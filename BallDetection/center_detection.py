import cv2 as cv
#import imutils as imutils
import numpy as np


def find_center(img):
    counter = 0
    row_sum = 0
    column_sum = 0

    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):
            r = img[i, j][2]
            if r != 0:
                counter += 1
                row_sum += i
                column_sum += j
    print("Red pixel: " + str(counter))
    center_y = np.rint(row_sum / counter)
    center_x = np.rint(column_sum / counter)
    print("Center: " + str(center_x) + " " + str(center_y))


img = cv.imread("roterball3.png")
img = small = cv.resize(img, (0,0), fx=0.5, fy=0.5)
#norm = cv.normalize(img, np.zeros(img.shape), 0, 255, cv.NORM_MINMAX)
#resized = imutils.resize(img, width=600)
#blurred = cv.GaussianBlur(resized, (11, 11), 0)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# "In HSV space, the red color wraps around 180. So you need the H values to be both in [0,10] and [170, 180]."
# https://stackoverflow.com/questions/32522989/opencv-better-detection-of-red-color

lower1_red = np.array([0,70,50])
upper1_red = np.array([10,255,255])

lower2_red = np.array([170,70,50])
upper2_red = np.array([180,255,255])

mask1 = cv.inRange(hsv, lower1_red, upper1_red)
mask2 = cv.inRange(hsv, lower2_red, upper2_red)

mask = cv.bitwise_or(mask1, mask2)

# "construct a mask for the color green, then perform
# a series of dilations and erosions to remove any small
# blobs left in the mask" (red)
# https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

mask = cv.erode(mask, None, iterations=5)
mask = cv.dilate(mask, None, iterations=5)
res = cv.bitwise_and(img, img, mask = mask)

cv.imwrite("res.png", res)
cv.imshow("res", res)
cv.waitKey(0)
find_center(res)