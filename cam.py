from picamera2 import Picamera2
from libcamera import controls
import os

mode = "/underaged/"

# folder path
dir_path = r'/home/admin/cam/underaged'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        buff = os.path.splitext(path)[0]
        res.append(buff)
print(res)

last = str(int(max(res))+1)
print(last)

picam2 = Picamera2()
picam2.start(show_preview=True)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
picam2.capture_file(mode + last +".jpg")
picam2.stop_preview()
picam2.stop()