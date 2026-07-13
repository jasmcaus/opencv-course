# pylint:disable=no-member

import cv2 as cv
import numpy as np

# Create blank image
img = np.zeros((500, 500, 3), dtype="uint8")

# ----------------------------
# Gradient Background
# ----------------------------
for i in range(500):
    color = (255 - i//3, 120 + i//4, 180)
    cv.line(img, (0, i), (500, i), color, 1)

# ----------------------------
# Decorative Border
# ----------------------------
cv.rectangle(img, (10, 10), (490, 490), (255, 255, 255), 3)
cv.rectangle(img, (20, 20), (480, 480), (0, 255, 255), 2)

# ----------------------------
# Filled Rectangle
# ----------------------------
cv.rectangle(img, (60, 60), (180, 180), (0, 255, 0), -1)

# ----------------------------
# Circle
# ----------------------------
cv.circle(img, (370, 120), 60, (0, 0, 255), -1)
cv.circle(img, (370, 120), 70, (255, 255, 255), 3)

# ----------------------------
# Triangle
# ----------------------------
pts = np.array([[250, 320], [180, 440], [320, 440]], np.int32)
cv.fillPoly(img, [pts], (255, 0, 255))

# ----------------------------
# Line Design
# ----------------------------
cv.line(img, (40, 260), (460, 260), (255, 255, 255), 2)
cv.line(img, (250, 40), (250, 460), (255, 255, 255), 2)

# ----------------------------
# Small Decorative Circles
# ----------------------------
for x in range(60, 461, 50):
    cv.circle(img, (x, 30), 8, (0, 255, 255), -1)
    cv.circle(img, (x, 470), 8, (0, 255, 255), -1)

# ----------------------------
# Text
# ----------------------------
cv.putText(img, "WELCOME!", (110, 230),
           cv.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 2)

cv.putText(img, "My name is Artdan",
           (100, 280),
           cv.FONT_HERSHEY_SIMPLEX,
           0.8,
           (0, 0, 0),
           4)

cv.putText(img, "My name is Artdan",
           (100, 280),
           cv.FONT_HERSHEY_SIMPLEX,
           0.8,
           (255, 255, 0),
           2)

# ----------------------------
# Show Image
# ----------------------------
cv.imshow("Creative OpenCV Design", img)

cv.waitKey(0)
cv.destroyAllWindows()# pylint:disable=no-member

import cv2 as cv
import numpy as np

# Create blank image
img = np.zeros((500, 500, 3), dtype="uint8")

# ----------------------------
# Gradient Background
# ----------------------------
for i in range(500):
    color = (255 - i//3, 120 + i//4, 180)
    cv.line(img, (0, i), (500, i), color, 1)

# ----------------------------
# Decorative Border
# ----------------------------
cv.rectangle(img, (10, 10), (490, 490), (255, 255, 255), 3)
cv.rectangle(img, (20, 20), (480, 480), (0, 255, 255), 2)

# ----------------------------
# Filled Rectangle
# ----------------------------
cv.rectangle(img, (60, 60), (180, 180), (0, 255, 0), -1)

# ----------------------------
# Circle
# ----------------------------
cv.circle(img, (370, 120), 60, (0, 0, 255), -1)
cv.circle(img, (370, 120), 70, (255, 255, 255), 3)

# ----------------------------
# Triangle
# ----------------------------
pts = np.array([[250, 320], [180, 440], [320, 440]], np.int32)
cv.fillPoly(img, [pts], (255, 0, 255))

# ----------------------------
# Line Design
# ----------------------------
cv.line(img, (40, 260), (460, 260), (255, 255, 255), 2)
cv.line(img, (250, 40), (250, 460), (255, 255, 255), 2)

# ----------------------------
# Small Decorative Circles
# ----------------------------
for x in range(60, 461, 50):
    cv.circle(img, (x, 30), 8, (0, 255, 255), -1)
    cv.circle(img, (x, 470), 8, (0, 255, 255), -1)

# ----------------------------
# Text
# ----------------------------
cv.putText(img, "WELCOME!", (110, 230),
           cv.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 2)

cv.putText(img, "My name is Artdan",
           (100, 280),
           cv.FONT_HERSHEY_SIMPLEX,
           0.8,
           (0, 0, 0),
           4)

cv.putText(img, "My name is Artdan",
           (100, 280),
           cv.FONT_HERSHEY_SIMPLEX,
           0.8,
           (255, 255, 0),
           2)

# ----------------------------
# Show Image
# ----------------------------
cv.imshow("Creative OpenCV Design", img)

cv.waitKey(0)
cv.destroyAllWindows()