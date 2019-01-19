import numpy as np
import io
import cv2

import picamera
from time import sleep

stream = io.BytesIO()

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format = 'jpeg')
    
buff = np.fromstring(stream.getvalue(), dtype = np.uint8)

img = cv2.imdecode(buff, 1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print "Found " + str(len(faces)) + " face(s)"

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
    
cv2.imwrite('result.jpg', img)
