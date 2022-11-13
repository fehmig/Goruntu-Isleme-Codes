import cv2 as cv2

img = cv2.imread("Pictures/picture3.jpg")
img_neg = cv2.imread("Pictures/picture3.jpg")

height, width, _ = img.shape
for i in range(0, height - 1):
    for j in range(0, width - 1):
        pixel = img_neg[i, j]
        pixel[0] = 255 - pixel[0]
        pixel[1] = 255 - pixel[1]
        pixel[2] = 255 - pixel[2]
        img_neg[i, j] = pixel

img_neg1 = 255 - img

cv2.imshow("Original", img)
cv2.imshow("negative_shortMethod", img_neg1)
cv2.waitKey(0)
cv2.destroyAllWindows()
