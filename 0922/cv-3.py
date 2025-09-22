import cv2
import os

os.makedirs('output', exist_ok=True)

img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_COLOR_8)

# 上下翻轉
# img = cv2.flip(img, 0)
# 左右翻轉
# img = cv2.flip(img, 1)
# 上下左右翻轉
# img = cv2.flip(img, -1)

# 旋轉180
# img = cv2.rotate(img, cv2.ROTATE_180)

# 順時針旋轉90
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# 逆時針旋轉90
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# 自訂旋轉
h,w = img.shape[:2]
rotate_matrix = cv2.getRotationMatrix2D((w//2,h//2),60,1)
rotate_img = cv2.warpAffine(img,rotate_matrix,(w,h))

cv2.imshow('test',rotate_img)
cv2.waitKey(0)
cv2.destroyWindow('test')