import os

src = "track3.txt" 

cam_files = {}

with open(src, "r") as f:
    for line in f:
        items = line.strip().split()
        if len(items) != 9:
            continue
        
        cam = int(items[0])         # camera_id
        gid = int(items[1])         # global_id
        frame = int(items[2])       # frame_id

        if cam not in cam_files:
            cam_files[cam] = open(f"cam_{cam}.txt", "w")
        
        cam_files[cam].write(line)

for f in cam_files.values():
    f.close()

print("Done! Get cam_*.txt")

