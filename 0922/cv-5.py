import glob, os
import cv2

os.makedirs('output', exist_ok=True)

imgs = glob.glob('./images/*.jpg')

count = 0

input_w = input('請輸入縮圖寬度：')
input_q = input('請輸入縮圖品質(0-100)：')
for img in imgs:
    result = cv2.imread(img,cv2.IMREAD_COLOR)

    h, w = result.shape[:2]

    resize_w = int(input_w)
    resize_h = int((h * resize_w) / w)

    img_resize = cv2.resize(result,(resize_w, resize_h))
    # fname = os.path.basename(img)
    fname,ext = os.path.splitext(img)
    fname = fname.split('\\')[1]
    print(fname,ext)
    if ext == '.jpg':
        cv2.imwrite(f'./output/small_{fname}{ext}',img_resize,[cv2.IMWRITE_JPEG_QUALITY,int(input_q)])


    # 顯示預覽
    # cv2.imshow(str(count), result)
    # cv2.imshow('hello', result)
    # cv2.waitKey(1000)
    count += 1

# cv2.destroyWindow('hello')
# cv2.destroyAllWindows()