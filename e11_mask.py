import numpy as np
import argparse
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# create numpy array filled with zeros with exact width and height of image
    # filling with zeros make the pixel black
# create a rectangular mask
mask = np.zeros(image.shape[:2], dtype = "uint8")  #here in image.shage[:2] is height and width of image.
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1) #-75 to 75 makes it 150 pixel - that is the width and height of rectangular mask
cv2.imshow("Mask", mask)

# AND operator will show the merged with AND ( common) area.
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow(" Masked image", masked)
cv2.waitKey(0)


# create numpy array filled with zeros with exact width and height of image
# create a circular mask
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow(" Masked image", masked)
cv2.waitKey(0)