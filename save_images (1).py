import cv2

vid  = cv2.VideoCapture(0)
i = 0
while True:
    ret, frame = vid.read()
    if ret:
        cv2.imwrite("image/image_{}_final.png".format(i), frame)
        cv2.imshow("result", frame)
        i+=1
        if cv2.waitKey(1) == 27 or i > 50:
            break
    else:
        print("Camera Not Found")
vid.release()
cv2.destroyAllWindows()