import numpy as np
import argparse
import cv2

### OpenCV has a way to find curves in an umage
### it uses contours- A contour is a curve of points with no gaps in the curve
### useful for shape analysis

###For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
###In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.
### . Contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.


# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

# convert image to greyscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(gray, (15,15), 0)

cv2.imshow("Gaussian blurr", blurred)

canny = cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny Edge Detected", canny)

# finding the contours, counting and marking them
### first Param: the edgy image
### Note: the findContours() function will alter the original image. So use a copy of image
### Second Param: Type of contour. Here we want external, so we use RETR_EXTERNAL
### 3rd Param: The type of approximation
### Returns a tuple, first is heirarchy- not used now.

( _, cnts, _ ) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("The number of coins in the image is : {}".format(len(cnts)))

#create a copy of the image
coins = image.copy()

# draw the contours in the actual color image copy
### 1st param: image source
### 2nd Param: the python's list of contours to draw
### 3rd paramL: index of contours- useful when you want to draw a partucular contour. Use -1 to draw all contours
### 4th is color
### 5th is thickness

cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Contours", coins)

cv2.waitKey(0)