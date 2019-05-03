import cv2
import numpy as np

image = cv2.imread("japan.png")

# Diese funktion geht durch alle Pixel und zählt die farbwerte für rot blau und grün 
# Momentanes Problem: weiße werte sind bei allen drei 255
# => nur wenn der größte wert rot ist wird counter hochgezählt
# Entfernung: Check

counter=0
for row in image:
    for column in row:
        blue =column[0]
        red = column[2]
        green = column[1]
        if(red>blue & red>green):
            counter += 1
print(counter)        
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()