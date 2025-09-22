import cv2

# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg')

# 讀取圖片，BGR模式
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_COLOR_BGR)
# 讀取圖片，RGB模式
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_COLOR_RGB)

# 讀取圖片，原始大小
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_COLOR)

# 讀取圖片，1/2大小
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_COLOR_2)

# 讀取圖片，1/4大小
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_COLOR_4)

# 讀取圖片，1/8大小
img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_COLOR_8)
# 讀取圖片，轉灰階
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_GRAYSCALE)

# 讀取圖片，轉灰階，1/2大小
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)

# 讀取圖片，轉灰階，1/4大小
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_4)

# 讀取圖片，轉灰階，1/8大小
# img = cv2.imread('./images/maksim-samuilionak-uymaeBza9KQ-unsplash.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_8)

cv2.imshow('test', img)


# 1秒鐘=1000毫秒，設定0為不關閉
# 關閉等待時間
cv2.waitKey(0)

cv2.destroyWindow('test')