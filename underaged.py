#!/usr/bin/python3
from picamera2 import Picamera2
from libcamera import controls
import os
import time

mode = "underaged"

# folder path
dir_path = r'/home/admin/cam/underaged/'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        buff = os.path.splitext(path)[0]
        res.append(buff)
print(res)
res=list(map(int, res))
maxnum=max(res)
print(maxnum)
plusone=int(maxnum)+1
print(plusone)
last = str(plusone) 
print(last)

picam2 = Picamera2()
picam2.options["quality"] = 95
config = picam2.create_still_configuration(main={'size': (4608, 2592) },
                                           lores={'size': (640, 480) },
                                           display='lores', buffer_count=3, queue=False)
picam2.configure(config)
picam2.start(show_preview=True)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous,
                     "AeFlickerMode":controls.AeFlickerModeEnum.Manual,
                     "AeFlickerPeriod":10000})
time.sleep(2)
picam2.capture_file(dir_path + last +".jpg")
picam2.stop_preview()
picam2.stop()