import argparse
import e5_imutils
import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])
cv2.imshow(" original image ", image)
cv2.waitKey(0)

#resize the image
resized = e5_imutils.resize(image, width = 500)
cv2.imshow(" width resized ", resized)
cv2.waitKey(0)

resized = e5_imutils.resize(image, height = 200)
cv2.imshow(" Height resized ", resized)
cv2.waitKey(0)