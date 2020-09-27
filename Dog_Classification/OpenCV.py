import numpy as np
import cv2

rgb_image = cv2.imread('./Welsh+corgi/0.png')
cv2.imshow('rgb_image', rgb_image)
cv2.waitKey(0)
# cv2.destroyAllWindows()