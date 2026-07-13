# pylint:disable=no-member

import cv2 as cv
import numpy as np

# Create blank image
blank = np.zeros((400, 400), dtype='uint8')

# -------------------------
# Star 1
# -------------------------
star1 = blank.copy()

pts1 = np.array([
    [200, 40],
    [230, 140],
    [340, 140],
    [250, 200],
    [290, 320],
    [200, 250],
    [110, 320],
    [150, 200],
    [60, 140],
    [170, 140]
], np.int32)

cv.fillPoly(star1, [pts1], 255)

# -------------------------
# Star 2 (Shifted)
# -------------------------
star2 = blank.copy()

pts2 = np.array([
    [230, 70],
    [260, 170],
    [370, 170],
    [280, 230],
    [320, 350],
    [230, 280],
    [140, 350],
    [180, 230],
    [90, 170],
    [200, 170]
], np.int32)

cv.fillPoly(star2, [pts2], 255)

# Display Stars
cv.imshow("Star 1", star1)
cv.imshow("Star 2", star2)

# Bitwise AND
bitwise_and = cv.bitwise_and(star1, star2)
cv.imshow("Bitwise AND", bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(star1, star2)
cv.imshow("Bitwise OR", bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(star1, star2)
cv.imshow("Bitwise XOR", bitwise_xor)

# Bitwise NOT
bitwise_not = cv.bitwise_not(star1)
cv.imshow("Bitwise NOT", bitwise_not)

cv.waitKey(0)
cv.destroyAllWindows()