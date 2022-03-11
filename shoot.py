import cv2
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11,50)
p.start(0)
#time.sleep(0.5)
def shoot():
    print("turning right")
    p.ChangeDutyCycle(1)
    time.sleep(1)
    print("turning right")
    p.ChangeDutyCycle(4)
    time.sleep(1)
    p.ChangeDutyCycle(1)






face_cascade = cv2.CascadeClassifier('haarcascade.xml');

video = cv2.VideoCapture(0);

while True:
    check, frame = video.read();
    faces = face_cascade.detectMultiScale(frame,
                                          scaleFactor=1.1, minNeighbors=5);
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3);
        shoot()
    cv2.imshow('Face Detector', frame);

    key = cv2.waitKey(1);

    if key == ord('q'):
        break;

video.release();
cv2.destroyAllWindows();
#Clean things up
p.stop()
GPIO.cleanup()
print("Good Bye")
