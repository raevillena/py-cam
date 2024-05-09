from picamera2 import Picamera2
from libcamera import controls
from os import walk

picam2 = Picamera2()
picam2.start(show_preview=True)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
picam2.capture_file("test6.jpg")
picam2.stop_preview()
picam2.stop()

filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file
print(filenames)