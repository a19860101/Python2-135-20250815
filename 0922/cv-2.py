import cv2
import os

os.makedirs('output', exist_ok=True)

img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg')

h, w, _ = img.shape
print(h,w)

resize_w = 400
resize_h = int((h * resize_w) / w)

img_resize = cv2.resize(img,(resize_w, resize_h))

cv2.imwrite('./output/001.jpg',img_resize,[cv2.IMWRITE_JPEG_QUALITY,1])

# jpeg 0-100
# cv2.imwrite('./output/001.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,80])

#png 0-9，數字越大，檔案越小，壓縮時間越長
# cv2.imwrite('./output/001.png',img,[cv2.IMWRITE_PNG_COMPRESSION,5])

#webp 0-100
# cv2.imwrite('./output/001.webp',img,[cv2.IMWRITE_WEBP_QUALITY,0])

#gif 0-100
# cv2.imwrite('./output/001.gif',img,[cv2.IMWRITE_GIF_QUALITY,255])


cv2.imshow('test',img_resize)
cv2.waitKey(0)
cv2.destroyWindow('test')