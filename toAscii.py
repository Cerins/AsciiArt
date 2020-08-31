import numpy as np
import cv2 as cv
import sys


if(len(sys.argv) != 2):
    raise Exception("Invalid amount of arguments passed")
    
img = cv.imread(sys.argv[1])
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
shades = " .:-=+*#%@"
rows,cols = img.shape
result = ""

for i in range(rows):
        for j in range(cols):
            result += shades[int(img[i,j]*len(shades)/(255))]
        result+="\n"

print(result)
