import cv2

# img = cv2.imread('./images/ysy_20250616_120900-696x522.jpg')
img = cv2.imread('./images/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
# img = cv2.imread('./images/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project.jpg')
face = cv2.imread('./images/face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.1,
                                      minNeighbors=5)



for (x,y,w,h) in faces:
    # face_area = img[y:y+h, x:x+w]
    face = cv2.resize(face, (w,h))
    img[y:y+h, x:x+w] = face


cv2.imshow('Face Detection',img)
cv2.waitKey(0)
cv2.destroyWindow('Face Detection')