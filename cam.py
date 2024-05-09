from picamera2 import Picamera2
from libcamera import controls


picam2 = Picamera2()
picam2.start(show_preview=True)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
picam2.capture_file("test6.jpg")
picam2.stop_preview()
picam2.stop()


import os

# folder path
dir_path = r'/home/admin/cam/overaged'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)