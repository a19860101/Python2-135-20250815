import cv2

img = cv2.imread('./images/ysy_20250616_120900-696x522.jpg')

img2 = img[100:200, 200: 400]
# [y1:y2, x1:x2]

h,w,_ = img2.shape

img2 = cv2.resize(img2, (w//20, h//20))
img2 = cv2.resize(img2, (w,h), interpolation=cv2.INTER_NEAREST)

# img2 = cv2.GaussianBlur(img2, (99,99), 3)

# img = cv2.GaussianBlur(img, (99,99), 3)

# cv2.imshow('test 1',img)
cv2.imshow('test 2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()