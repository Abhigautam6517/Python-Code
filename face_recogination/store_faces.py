import cv2
import numpy as np
vid  = cv2.VideoCapture(0)
dataset = cv2.CascadeClassifier("data.xml")
i = 0
face_list = []
while True:
    ret, frame = vid.read()
    if ret:
        print(i)
        i+=1
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = dataset.detectMultiScale(frame, 1.2)
        for x,y,w,h in faces:
            face = frame[y:y+h, x:x+w]
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255,0), 2)
        cv2.imwrite("face.png", face)
        face = cv2.resize(face, (50, 50))
        face_list.append(face)
        cv2.imshow("result", frame)
        if cv2.waitKey(1) == 27 or i == 49:
            break
    else:
        print("Camera Not Found")
np.save("faces/user_1.npy", np.array(face_list))
vid.release()
cv2.destroyAllWindows()