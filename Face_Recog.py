import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images 
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

motorEna = 2
motorIn1 = 3
motorIn2 = 4

GPIO.setup(motorEnA,  GPIO.OUT)
GPIO.setup(motorIn1,  GPIO.OUT)
GPIO.setup(motorIn2,  GPIO.OUT)

def unlock():
    print("kilit acildi... \n")
    
    GPIO.output(motorIn1, GPIO.HIGH)
    GPIO.output(motorIn2, GPIO.LOW)
    GPIO.output(motorEnA, GPIO.HIGH)
    sleep(2)
    GPIO.output(motorEnA, GPIO.LOW)
    
labels = ["zeynep","yetkin"] 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.load("face-trainner.yml")   in opencv 3.x; load() -> replaced with read() 
recognizer.read("face-trainner.yml")

cap = cv2.VideoCapture(0) 

while(True):

    ret, img = cap.read() # Break video into frames 
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Recog. faces
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

        id_, conf = recognizer.predict(roi_gray) #recognize the Face
    
        if conf>=80:
            font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name 
            name = labels[id_] #Get the name from the List using ID number 
            cv2.putText(img, name, (x,y), font, 1, (0,0,255), 2)
            if(name == "zeynep"):
                unlock()
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        
    cv2.imshow('Preview',img) #Display the Video
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
