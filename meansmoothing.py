import cv2
import numpy as np

# Reading the image
image = cv2.imread('americano-image.png')

# Applying the filter
averageBlur = cv2.blur(image, (5, 5))

# Showing the image
cv2.imshow('Original', image)
cv2.imshow('Average blur', averageBlur)

cv2.waitKey()
cv2.destroyAllWindows()
