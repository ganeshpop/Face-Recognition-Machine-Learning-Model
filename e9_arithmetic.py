import numpy as np
import argparse
import e5_imutils
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
#cv2.waitKey(0)


#1. The pixel value cannot be outside 0 and 255
#2. numpy performs a modulo operation. i.e., 10+250= 4
#3. openCV perform clipping . eg. 10+250 = 255. This is to protect values going beyond the range


#Arithmatic using openCV
print("max of 255 by cv2: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0 by cv2: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

#Arithmatic using numpy
print("wrap of max by np: {}".format(np.uint8([200])+np.uint8([100])))
print("wrap of min by np: {}".format(np.uint8([50])-np.uint8([100])))


#generating one array and multiplying it with 100
#adding that array to the actual image numpy array

# image.shape is the shape of image.
# np.ones(image.shape ...)  will generate an array of same shape of image, but with values as ones
# if image matix is like
#  x x x x 
#  x x x x 
#  x x x x 
#  x x x x 
#then np.ones of image.shage will produce
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
M = np.ones(image.shape, dtype = "uint8") * 100

#multiplying it by 100 it becomes
# 100 100 100 100
# 100 100 100 100
# 100 100 100 100
# 100 100 100 100
added = cv2.add(image, M)
cv2.imshow("Added image", added)
#the above code added 100 to every pixel value


#generating one array and multiplying it with 50
#substracting that array to the actual image numpy array
M = np.ones(image.shape, dtype = "uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted image", subtracted)

cv2.waitKey(0)








