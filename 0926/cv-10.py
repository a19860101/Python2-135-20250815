import cv2

img = cv2.imread('./images/ysy_20250616_120900-696x522.jpg')
# img = cv2.imread('./images/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
# img = cv2.imread('./images/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project.jpg')
# img = cv2.imread('./images/Doraemon_Charactor.jpg')
# img = cv2.imread('./images/250px-Nobi_Nobita.png')
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg', cv2.IMREAD_REDUCED_COLOR_8)
# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 載入 opecCV提供的預訓練人臉分類器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print(face_cascade)

faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.2,
                                      minNeighbors=5)

print(faces)

for (x,y,w,h) in faces:
    print(x,y,w,h)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(img,
                '大鼓祥平',
                (x, y - 5 ),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                1)

cv2.imshow('Face Detection',img)
cv2.waitKey(0)
cv2.destroyWindow('Face Detection')

"""
FONT_HERSHEY_SIMPLEX：正常大小無襯線字體、
FONT_HERSHEY_PLAIN：小號無襯線字體、
FONT_HERSHEY_DUPLEX：正常大小無襯線字體，比FONT_HERSHEY_SIMPLEX複雜一點、
FONT_HERSHEY_COMPLEX：正常大小有襯線字體、
FONT_HERSHEY_TRIPLEX：正常大小有襯線字體，比FONT_HERSHEY_COMPLEX複雜一點、
FONT_HERSHEY_COMPLEX_SMALL：FONT_HERSHEY_COMPLEX的小號、
FONT_HERSHEY_SCRIPT_SIMPLEX：手寫風格細體、
FONT_HERSHEY_SCRIPT_COMPLEX：手寫風格粗體，
"""