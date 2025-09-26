import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

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

# 使用 PIL 在指定位置加中文文字到 OpenCV 圖片
def put_chinese_text_cv2(img, text, position, font_path, font_size, color=(0, 255, 0), thickness=1):
    # 創建 PIL 圖像
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)

    # 載入字體
    font = ImageFont.truetype(font_path, font_size)

    # 加文字
    draw.text(position, text, font=font, fill=color)

    # 轉換回 OpenCV 格式
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)


for (x, y, w, h) in faces:
    print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    img = put_chinese_text_cv2(img,
                               '大鼓祥平',
                               (x, y - 21),
                               './Huninn-Regular.ttf',
                               16,
                               (0, 255, 0),
                               1)

cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyWindow('Face Detection')

# 字體下載 https://fonts.google.com/
