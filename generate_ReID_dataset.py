import os
import cv2

BASE_DIR = "."
# output ReID img path：In this train folder，build Aic/image_train
OUTPUT_DIR = "../Aic/image_train"


def load_gt(gt_path):
    """read gt.txt，return {frame_id: [(pid, x, y, w, h), ...]}"""
    gt = {}
    with open(gt_path, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) < 6:
                continue

            frame = int(parts[0])
            pid = int(parts[1])
            x = int(float(parts[2]))
            y = int(float(parts[3]))
            w = int(float(parts[4]))
            h = int(float(parts[5]))

            if pid == -1:
                continue  

            gt.setdefault(frame, []).append((pid, x, y, w, h))
    return gt


def process_camera(cam_folder, camid):
   
    cam_dir = os.path.join(BASE_DIR, cam_folder)
    print(f"\n[INFO] Processing camera {camid}: {cam_dir}")

    video_path = os.path.join(cam_dir, "vdo.avi")
    gt_path = os.path.join(cam_dir, "gt", "gt.txt")

    if not os.path.exists(video_path):
        print(f"[WARNING] Video not found: {video_path}, skip.")
        return

    if not os.path.exists(gt_path):
        print(f"[WARNING] GT not found: {gt_path}, skip.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[ERROR] Cannot open video: {video_path}")
        return

    gt = load_gt(gt_path)
    frame_idx = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx in gt:
            for pid, x, y, w, h in gt[frame_idx]:
                crop = frame[y:y + h, x:x + w]
                if crop.size == 0:
                    continue

                name = f"{pid}_c{camid}_{frame_idx:06d}.jpg"
                save_path = os.path.join(OUTPUT_DIR, name)
                cv2.imwrite(save_path, crop)

        frame_idx += 1

    cap.release()
    print(f"[DONE] Camera {camid} finished.")


def main():
    print("[INFO] Working directory:", os.getcwd())
    print("[INFO] Base dir (S01):", os.path.abspath(BASE_DIR))

    cam_folders = sorted(
        d for d in os.listdir(BASE_DIR)
        if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("c")
    )

    if not cam_folders:
        print("[ERROR] No camera folders (cXXX) found in", os.path.abspath(BASE_DIR))
        return

    print("[INFO] Found cameras:", cam_folders)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("[INFO] Output dir:", os.path.abspath(OUTPUT_DIR))

    for camid, cam_folder in enumerate(cam_folders, start=1):
        process_camera(cam_folder, camid)

    print("\n[INFO] All cameras processed.")


if __name__ == "__main__":
    main()

