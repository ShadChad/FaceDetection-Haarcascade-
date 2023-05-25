import cv2

# video_cap = cv2.VideoCapture(0)
# while True:
#     ret,video_data= video_cap.read()

#     cv2.imshow("video_live",video_data)
#     if cv2.waitKey(10) == ord("a"):
#         break
#     video_cap.release()


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0) #can put filename, or 0 for webcam

while True:
    _,img = cap.read()



# img = cv2.imread('C:\\Users\\subed\\Desktop\\python 100 days of code\\Exercise\\face_detection\\img.jpg')

    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # print(grey)
    faces = face_cascade.detectMultiScale(grey,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
























