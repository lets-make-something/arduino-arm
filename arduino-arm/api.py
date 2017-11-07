import serial
import time
import numpy as np
import cv2

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
while(True):
    # Capture frame-by-frame
    ret, img = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



#img = cv2.imread('sachin.jpg')
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

class Arm:
    def __init__(self):
        self.connect = serial.Serial('COM3',9600,timeout=0.1)

        print(self.connect.readline());
        print(self.connect.dtr);

        self.pwm_max = 530
        self.pwm_min = 130

    def write(self,i,degree):
        pwm = (self.pwm_max-self.pwm_min)*degree/180 + self.pwm_min
        str = '{} {}\n'.format(i, pwm)
        print(str)
        print(self.connect.dtr);
        self.connect.write(str.encode('utf-8'))
        self.connect.flush()
        print(self.connect.dtr);
        print(self.connect.readline());
    def openhand(self):
        self.write(5,90)
        self.write(4,25)
    def closehand(self):
        self.write(5,50)
        self.write(4,70)
    def down(self):
        self.write(0,90)
        self.write(1,145)
        self.write(2,30)
        self.write(3,90)
    def up(self):
        self.write(0,90)
        self.write(1,120)
        self.write(2,60)
        self.write(3,90)
    def up2(self):
        self.write(0,90)
        self.write(1,80)
        self.write(2,10)
        self.write(3,90)
    def one(self):
        return 1

