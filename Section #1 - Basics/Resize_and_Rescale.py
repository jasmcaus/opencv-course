#pylint:disable=no-member

# Resizing and Rescaling can be done for images/videos/live videos
# Resizing and rescaling is needed to prevemt computational strain due to large files
# Resize is basically modifying height and width to a particular scale. Generally we downscale coz our devices are generally incapable of going higher, say from 720p to 1080p

import cv2 as cv

img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)


def changeRes(width,height):
    # Live Videos
    # These integer arguments are the properties of capture class.
    # 3 references width
    # 4 references height
    # 10 references brightness
    capture.set(3, width)   
    capture.set(4, height)

resized_image = rescaleFrame(img,scale=0.2)
cv.imshow('Image resized', resized_image)


#Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('video', frame)
    cv.imshow('video Resized', frame_resized)


    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows
