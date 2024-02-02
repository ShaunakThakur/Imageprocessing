import cv2
import numpy as np
from skimage.util import random_noise

# Reading the image
image = cv2.imread('americano-image.png')

blur = cv2.bilateralFilter(image,20,200,300)

# Showing the image
cv2.imshow('Original', image)
cv2.imshow('Bilateral Blur', blur)

cv2.waitKey()
cv2.destroyAllWindows()