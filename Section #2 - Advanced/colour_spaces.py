# pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt

# Load image
img = cv.imread("../Resources/Photos/jiraya.jpg")

# Check if image exists
if img is None:
    print("Error: Could not load image.")
    exit()

# Display original image
cv.imshow("Original Image", img)

# Convert to different color spaces
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab_img = cv.cvtColor(img, cv.COLOR_BGR2LAB)
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
hls_img = cv.cvtColor(img, cv.COLOR_BGR2HLS)

# Show converted images
cv.imshow("Grayscale", gray_img)
cv.imshow("HSV", hsv_img)
cv.imshow("LAB", lab_img)
cv.imshow("RGB", rgb_img)
cv.imshow("HLS", hls_img)

# Convert RGB back to BGR
bgr_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2BGR)
cv.imshow("RGB to BGR", bgr_img)

# Display image using Matplotlib
plt.figure(figsize=(7, 5))
plt.imshow(rgb_img)
plt.title("Jiraiya in RGB")
plt.axis("off")
plt.tight_layout()
plt.show()

# Wait and close all windows
cv.waitKey(0)
cv.destroyAllWindows()