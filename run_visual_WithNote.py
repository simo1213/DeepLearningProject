import cv2
import numpy as np
from glob import glob

resize_w, resize_h = 640, 360   # camera size after smaller
grid_cols = 3
grid_rows = 2   # 6 cameras


def get_color(gid):
    np.random.seed(gid)  # same gid have same color,diff-gid have diff-color
    r, g, b = np.random.randint(0, 255, size=3)
    return (int(r), int(g), int(b))


# read cam_*.txt
track_files = sorted(glob("cam_*.txt"))

if len(track_files) != 6:
    print("finding camera number ≠ 6，actually finding number：", len(track_files))

print("the track file name we get：", track_files)


# load all ID
# tracks[i][frame] = [(gid, x, y, w, h)]
tracks = []
for tf in track_files:
    dic = {}
    with open(tf) as f:
        for line in f:
            cam, gid, frame, x, y, w, h, _, _ = map(int, line.split())
            if frame not in dic:
                dic[frame] = []
            dic[frame].append((gid, x, y, w, h))
    tracks.append(dic)


# match video_XX.avi
videos = [f"video_{tf.split('_')[1].split('.')[0]}.avi" for tf in track_files]
caps = [cv2.VideoCapture(v) for v in videos]

print("Match video：", videos)

fps = caps[0].get(cv2.CAP_PROP_FPS)

out_w = resize_w * grid_cols
out_h = resize_h * grid_rows + 50   # in Top add 50 px note

fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = cv2.VideoWriter("all_gid_color_multicam_banner.avi", fourcc, fps, (out_w, out_h))

print(f"Output video size: {out_w} × {out_h}")

frame_id = 0


# ========== Visualize ==========
while True:
    frames = []
    ids_in_frame = []  

    for cap, dic in zip(caps, tracks):
        ret, frame = cap.read()
        if not ret:
            frames.append(None)
            ids_in_frame.append([])
            continue
        
        frame = cv2.resize(frame, (resize_w, resize_h))

        cam_ids = []

        if frame_id in dic:
            for gid, x, y, w, h in dic[frame_id]:
                cam_ids.append(gid)

                scale_x = resize_w / cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                scale_y = resize_h / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

                x = int(x * scale_x)
                y = int(y * scale_y)
                w = int(w * scale_x)
                h = int(h * scale_y)

                color = get_color(gid)

                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, f"id:{gid}", (x, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        ids_in_frame.append(cam_ids)
        frames.append(frame)

    if all(f is None for f in frames):
        break

    for i in range(len(frames)):
        if frames[i] is None:
            frames[i] = np.zeros((resize_h, resize_w, 3), dtype=np.uint8)

    row1 = np.hstack(frames[:3])
    row2 = np.hstack(frames[3:6])
    combined = np.vstack([row1, row2])

    banner = np.zeros((50, out_w, 3), dtype=np.uint8)
    banner[:] = (30, 30, 30)  

    # If global_id appera >= 2cameras, show it in note
    all_ids = [gid for cam_list in ids_in_frame for gid in cam_list]
    multi_ids = [gid for gid in set(all_ids) if sum([gid in cam_list for cam_list in ids_in_frame]) > 1]

    if len(multi_ids) == 0:
        text = "No multi-view objects"
    else:
        multi_ids_str = ", ".join(str(i) for i in sorted(multi_ids))
        text = f"Multi-view IDs: {multi_ids_str}"

    cv2.putText(banner, text, (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    final_frame = np.vstack([banner, combined])

    writer.write(final_frame)
    frame_id += 1


for c in caps:
    c.release()
writer.release()

print("Finish：all_gid_color_multicam_withNote.avi")

