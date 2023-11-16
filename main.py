import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

Video_capture = cv2.VideoCapture(0)

prakhars_image = face_recognition.load_image_file("")



#face detector model
face_detector = dlib.get_frontal_face_detector()

#capture frames continously
while True:
    ret,frame= cap.read()
    frame =cv2.flip(frame,1)

    #RGB -> Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    #Interate through all the faces and draw rectangle around each face and also number it
    i=0
    for face in faces :
        #Find the co-ordinate of the face
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()

        #draw the rectangle
        cv2.rectangle(frame,(x,y),(x1,y1), (0, 255, 0), 2)

        i=i+1

        cv2.putText(frame, "Face num"+ str(i), (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

    cv2.imshow('frame', frame)

    #code to come out of the infinite loop / interrupt the execution
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()