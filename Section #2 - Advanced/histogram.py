# pylint:disable=no-member

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load image
photo = cv.imread("../Resources/Photos/venom.jpg")

# Check if image exists
if photo is None:
    print("Error: Image not found.")
    exit()

cv.imshow("Original Image", photo)

# Create a blank mask
mask = np.zeros(photo.shape[:2], dtype="uint8")

# Create a rounded rectangle mask
cv.rectangle(mask, (100, 80), (350, 320), 255, -1)
cv.circle(mask, (100, 80), 40, 255, -1)
cv.circle(mask, (350, 80), 40, 255, -1)
cv.circle(mask, (100, 320), 40, 255, -1)
cv.circle(mask, (350, 320), 40, 255, -1)

cv.imshow("Rounded Rectangle Mask", mask)

# Apply mask
result = cv.bitwise_and(photo, photo, mask=mask)
cv.imshow("Masked Image", result)

# Plot color histogram
plt.figure(figsize=(8, 5))
plt.title("RGB Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

colors = ("b", "g", "r")

for i, color in enumerate(colors):
    hist = cv.calcHist([photo], [i], mask, [256], [0, 256])
    plt.plot(hist, color=color)

plt.xlim([0, 256])
plt.grid(True)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()