import numpy as np
import argparse
import cv2
# Canny edge is a multi step process
# uses blur to remove noise
# uses thresholding to find if pixel is edge eligible or not
# 
# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# implement gaussian blurr
blurred = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Gaussian blurr", blurred)


# the second parameter is threshold 1 and third is threshold 2
# any gradient value below threshold1 will be evaluated as NOT an Edge
# any gradient value above threshold2 will be evaluated as NOT an Edge
# only those between thereshold1 and threshold2 are evaluated as Edge
canny = cv2.Canny(blurred, 120, 150)
cv2.imshow("Canny Edge Detected", canny)
cv2.waitKey(0)