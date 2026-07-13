# pylint:disable=no-member

import cv2 as cv
import numpy as np

# Load image
image = cv.imread("../Resources/Photos/pain.jpg")

# Check if image exists
if image is None:
    print("Error: Image not found.")
    exit()

cv.imshow("Original Image", image)

# Create blank mask
mask = np.zeros(image.shape[:2], dtype="uint8")

# Draw an ellipse
ellipse = cv.ellipse(
    mask.copy(),
    (image.shape[1] // 2, image.shape[0] // 2),
    (140, 90),
    0,
    0,
    360,
    255,
    -1
)

# Draw a triangle
triangle = mask.copy()
points = np.array([
    [image.shape[1] // 2, 40],
    [80, image.shape[0] - 40],
    [image.shape[1] - 80, image.shape[0] - 40]
], np.int32)

cv.fillPoly(triangle, [points], 255)

# Combine the shapes
custom_mask = cv.bitwise_and(ellipse, triangle)
cv.imshow("Custom Mask", custom_mask)

# Apply the mask
masked_image = cv.bitwise_and(image, image, mask=custom_mask)
cv.imshow("Masked Image", masked_image)

cv.waitKey(0)
cv.destroyAllWindows()
