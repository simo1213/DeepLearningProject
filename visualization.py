import cv2
import os
import sys

def draw_bbox(frame, bbox, obj_id, color=(0, 255, 0)):
    x, y, w, h = bbox
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    cv2.putText(frame, str(obj_id), (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

def load_gt(gt_path):
    gt_dict = {}
    with open(gt_path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) < 6:
                continue
            frame = int(parts[0])
            obj_id = int(parts[1])
            x, y, w, h = map(int, map(float, parts[2:6]))
            gt_dict.setdefault(frame, []).append((obj_id, (x, y, w, h)))
    return gt_dict

def visualize(video_path, gt_path):
    if not os.path.exists(video_path):
        print("[ERROR] Video not found:", video_path)
        sys.exit(1)

    if not os.path.exists(gt_path):
        print("[ERROR] GT not found:", gt_path)
        sys.exit(1)

    print("[OK] Video:", video_path)
    print("[OK] GT:", gt_path)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("[ERROR] Cannot open video:", video_path)
        sys.exit(1)

    gt_dict = load_gt(gt_path)
    frame_id = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video ended.")
            break

        if frame_id in gt_dict:
            for obj_id, bbox in gt_dict[frame_id]:
                draw_bbox(frame, bbox, obj_id)

        cv2.imshow("CityFlow GT Visualization", frame)

        key = cv2.waitKey(30)
        if key == ord('q'):
            break
        elif key == ord('p'):
            cv2.waitKey(0)

        frame_id += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Since this script is inside c001 folder, use relative paths
    cam_folder = "."

    video_path = os.path.join(cam_folder, "vdo.avi")
    gt_path = os.path.join(cam_folder, "gt/gt.txt")

    visualize(video_path, gt_path)

