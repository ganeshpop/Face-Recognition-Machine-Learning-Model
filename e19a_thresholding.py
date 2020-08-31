import numpy as np
import argparse
import cv2


# What is Thresholding of Image?
# Convert an image to binary is thresholding
# Take a grayscale image. It has pixel values from 0 to 255. 
# Now, lets take a thresholding value of a pixel as t . All values less than p are converted to 0 and greater than p are converted to 255.


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

# 1st type of thresholding
#simple Thresholding using binary
# here the threshold value is manually specified to 155. 155 will also be returned by cv2.threshold function and stored in T in this case
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

#simple Thresholding using inv binary
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Inv Binary", threshInv)

cv2.imshow("Only Coins", cv2.bitwise_and(image, image, mask = threshInv))


#adaptive thresholding using mean
# Here we dont need to specify the threshold value.
# its considered and it is practically better
# 2nd Arg is the maximum value
# 3rd arg is the type of threshold
# 4th is the inversion of threshold
# 5th is the neghbourshood size. It is the number of pixels around it to calculate the mean
# 6th arg is the called C, which is a constant value that you can add or substract from the mean to fine tune it.
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive mean", thresh)

#adaptive thresholding using gaussian
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Adaptive gaussian", thresh)

cv2.waitKey(0)