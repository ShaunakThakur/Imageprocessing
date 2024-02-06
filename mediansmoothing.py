import cv2
import numpy as np
from skimage.util import random_noise

# Reading the image
image = cv2.imread('americano-image.png')
## adding noise
noise_img = random_noise(image, mode='s&p',amount=0.3)
noise_img = np.array(255*noise_img, dtype = 'uint8')
## median filter
median = cv2.medianBlur(noise_img,5)
# Showing the image
cv2.imshow('Original', noise_img)
cv2.imshow('Median Blur', median)

cv2.waitKey()
cv2.destroyAllWindows()