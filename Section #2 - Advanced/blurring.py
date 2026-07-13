# pylint:disable=no-member

import cv2 as cv

# Load the image
image = cv.imread("../Resources/Photos/pain.jpg")

# Check if the image exists
if image is None:
    print("Error: Could not load the image. Check the file path.")
    exit()

# Display original image
cv.imshow("Original Image", image)

# Average Blur
average_blur = cv.blur(image, (5, 5))
cv.imshow("Average Blur", average_blur)

# Gaussian Blur
gaussian_blur = cv.GaussianBlur(image, (5, 5), 0)
cv.imshow("Gaussian Blur", gaussian_blur)

# Median Blur
median_blur = cv.medianBlur(image, 5)
cv.imshow("Median Blur", median_blur)

# Bilateral Filter
bilateral_filter = cv.bilateralFilter(image, 15, 75, 75)
cv.imshow("Bilateral Filter", bilateral_filter)

# Wait for a key press
cv.waitKey(0)
cv.destroyAllWindows()