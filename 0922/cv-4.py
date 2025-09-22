import cv2
import os

os.makedirs('output', exist_ok=True)

img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_COLOR_8)

# 矩形
cv2.rectangle(img,(200,200),(400,400),(255,0,0),5)

# 圓形
cv2.circle(img,(200,200),50,(128,100,60),4)

# 線
cv2.line(img,(200,200),(400,400),(0,0,255),5)

# 箭頭
cv2.arrowedLine(img,(100,300),(200,200),(0,255,0),5)

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyWindow('test')