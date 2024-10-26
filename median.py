import cv2





image=cv2.imread('img/balloons_noisy.png')

median=cv2.medianBlur(image,5)



cv2.imshow("medianImage",median)







cv2.waitKey(0)