import cv2
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img =cv2.imread("Woman.jpg")
print(img)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
scaleFactor = 1.05,
minNeighbours = 5)

for x,y,z,q in faces:
    img= cv2.rectangle(img, (x,y),(x+z,y+q),(0,255,0),3)

print(type(faces))
print(faces)
cv2.imshow("Gray",gray_img)
cv2.waitkey(0)
cv2.destroyAllWindows()
