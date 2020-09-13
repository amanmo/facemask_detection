import numpy as np
import cv2

#Initializing camera
cameraFeed = cv2.VideoCapture(0)

while True:

    #Reading camera input and converting to grayscale
    _, img = cameraFeed.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Loading HAAR cascades
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    mask_cascade = cv2.CascadeClassifier("haarcascade_facemask.xml")

    #Detecting faces and masks
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.25, minNeighbors = 3, minSize = (50,50))
    masks = mask_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 6, minSize = (50,50))
    
    #Visualizing the location of faces and masks
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 1)
        cv2.putText(img, "Unmasked", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))

    for (x,y,w,h) in masks:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 1)
        cv2.putText(img, "Masked", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))

    #Displaying output
    cv2.imshow("Camera", img)
    
    #Press q to exit
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()