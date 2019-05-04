import cv2 as cv
import numpy as np


def find_center(img):
    counter = 0
    max_value = 0
    row_sum = 0
    column_sum = 0
    # Hardcoded for japan.png image
    # TODO Remove
    white = [255, 255, 255]

    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):
            if not (np.array_equal(img[i, j], (white))):
                b, g, r = img[i, j]
                max_value = max(b, g, r)
                if max_value == r:
                    counter += 1
                    row_sum += i
                    column_sum += j
    print("Red pixel: " + str(counter))
    center_y = np.rint(row_sum / counter)
    center_x = np.rint(column_sum / counter)
    print("Center: " + str(center_x) + " " + str(center_y))


image = cv.imread("japan.png")
norm = np.zeros(image.shape)
norm = cv.normalize(image,  norm, 0, 255, cv.NORM_MINMAX)
#cv.imshow('img', norm)
#cv.waitKey(0)
#cv.destroyAllWindows()
find_center(norm)

