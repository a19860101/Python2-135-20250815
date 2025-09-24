import cv2

img = cv2.imread('./images/ysy_20250616_120900-696x522.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.2,
                                      minNeighbors=5)

for (x,y,w,h) in faces:
    mosaic = img[y:y+h, x:x+w]

    # 馬賽克
    level = 20
    mosaic = cv2.resize(mosaic,(w//level,h//level))
    mosaic = cv2.resize(mosaic, (w,h), interpolation=cv2.INTER_NEAREST)

    # 高斯模糊
    # mosaic = cv2.GaussianBlur(mosaic,(99,99), 10)

    img[y:y+h, x:x+w] = mosaic

cv2.imshow('Face Detection',img)
cv2.waitKey(0)
cv2.destroyWindow('Face Detection')