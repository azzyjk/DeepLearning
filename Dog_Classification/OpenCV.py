import numpy as np
import cv2
import imutils
import dlib 

rgb_image = cv2.imread('./Welsh+corgi/0.png') # 사진 불러오기
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY) # 사진 회색으로 변경하기
gray_image_blurred = cv2.GaussianBlur(gray_image, (5,5), 0)
cv2.imshow('rgb_image', rgb_image)
cv2.imshow('gray_image', gray_image)
cv2.imshow('blurred_image', gray_image_blurred)
cv2.waitKey(0)
