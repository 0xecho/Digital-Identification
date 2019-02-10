import numpy as np
import cv2 as cv
import numpy

def detect_face(img_path):
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
    img = cv.imdecode(numpy.fromstring(img_path.read(), numpy.uint8), cv.IMREAD_UNCHANGED)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    if len(faces)==1:
        return True
    else:
        return False
