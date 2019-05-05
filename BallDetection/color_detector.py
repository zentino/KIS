import cv2 as cv
import numpy as np

class ColorDetector:
    def detectColorFast(self, detectionimage):
        image = self.prepareImage(detectionimage)
        counter=0
        for row in image:
            for column in row:
                blue, green, red = column
                if(red>blue):
                    if(red>green):
                        counter += 1
        return counter
    def detectColorPrecise(self, detectionimage):
        img= self.prepareImage(detectionimage)
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
        return counter
    def isCenter(self, detectionimage):
        img= self.prepareImage(detectionimage)
        row= int(img.shape[0]/2)
        col= int(img.shape[1]/2)
        center= img[row,col]
        print(center)
        blue, green, red = center
        if(red>blue):
            if(red>green):
                return True
            else:
                return False
        else:
            return False
    def prepareImage(self, detectionimage):
        img = cv.imread(detectionimage)
        img = cv.resize(img, (0,0), fx=0.5, fy=0.5)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        lower1_red = np.array([0,70,50])
        upper1_red = np.array([10,255,255])
        lower2_red = np.array([170,70,50])
        upper2_red = np.array([180,255,255])
        mask1 = cv.inRange(hsv, lower1_red, upper1_red)
        mask2 = cv.inRange(hsv, lower2_red, upper2_red)
        mask = cv.bitwise_or(mask1, mask2)
        mask = cv.erode(mask, None, iterations=5)
        mask = cv.dilate(mask, None, iterations=5)
        res = cv.bitwise_and(img, img, mask = mask) 
        return res


# only to test the class
red= ColorDetector()
print(red.detectColorFast("roterball3.png"))        
print(red.detectColorPrecise("roterball3.png"))
print(red.isCenter("japan.png"))