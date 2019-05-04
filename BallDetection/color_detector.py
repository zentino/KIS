import cv2
import numpy as np

class ColorDetector:
    def detectColor(self, detectionimage):
        image = cv2.imread(detectionimage)
        counter=0
        for row in image:
            for column in row:
                blue, green, red = column
                if(green>blue):
                    if(green>red):
                        counter += 1
        return counter
    def isCenter(self):
        return True

# only to test the class
yellow= ColorDetector()
# value should be 0 because in the japanese flag is no yellow or green
print(yellow.detectColor("japan.png"))        
