# pylint:disable=no-member

import cv2 as cv
import numpy as np

# Load image
image = cv.imread("../Resources/Photos/nagato.jpg")

# Check if the image was loaded
if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Display original image
cv.imshow("Original Image", image)

# Create a blank single-channel image
blank = np.zeros(image.shape[:2], dtype="uint8")

# Split the image into Blue, Green, and Red channels
blue_channel, green_channel, red_channel = cv.split(image)

# Create images showing each color channel
blue_image = cv.merge([blue_channel, blank, blank])
green_image = cv.merge([blank, green_channel, blank])
red_image = cv.merge([blank, blank, red_channel])

# Display color channels
cv.imshow("Blue Channel", blue_image)
cv.imshow("Green Channel", green_image)
cv.imshow("Red Channel", red_image)

# Print image dimensions
print("Original Image Shape:", image.shape)
print("Blue Channel Shape:", blue_channel.shape)
print("Green Channel Shape:", green_channel.shape)
print("Red Channel Shape:", red_channel.shape)

# Merge channels back into one image
merged_image = cv.merge([blue_channel, green_channel, red_channel])
cv.imshow("Merged Image", merged_image)

cv.waitKey(0)
cv.destroyAllWindows()