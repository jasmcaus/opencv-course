# pylint:disable=no-member

import cv2 as cv
import numpy as np

# Load image
image = cv.imread("../Resources/Photos/kakashi.jpg")

# Check if image was loaded successfully
if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Display original image
cv.imshow("Original Image", image)

# Convert to grayscale
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray_image)

# Laplacian Edge Detection
laplacian = cv.Laplacian(gray_image, cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)
cv.imshow("Laplacian", laplacian)

# Sobel X
sobel_x = cv.Sobel(gray_image, cv.CV_64F, 1, 0)
sobel_x = cv.convertScaleAbs(sobel_x)

# Sobel Y
sobel_y = cv.Sobel(gray_image, cv.CV_64F, 0, 1)
sobel_y = cv.convertScaleAbs(sobel_y)

# Combine Sobel
sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel Y", sobel_y)
cv.imshow("Combined Sobel", sobel)

# Canny Edge Detection
canny = cv.Canny(gray_image, 100, 200)
cv.imshow("Canny", canny)

cv.waitKey(0)
cv.destroyAllWindows()