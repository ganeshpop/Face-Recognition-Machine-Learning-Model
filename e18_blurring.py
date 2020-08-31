import numpy as np
import argparse
import cv2
# WHY BLUR??
# Computer Vision function like thresholding and edge detection works better 
# if bllurring is performed

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])

# TYPE OF BLURRING
# 1. Averaging 
	# A k x k sliding window(called kernel) slides on top of image. , k is always odd number
	#. Slide Direction: Left to Right and then Top to Down
	#. The pixel at the center of matris is taken as the average of all surrounding pixels
	#. increasing the size of kernel increases the blurness

#average blurring.. hstack puts the image in horizontal stack, easy to refer
blurred = np.hstack([
	cv2.blur(image, (3,3)),
	cv2.blur(image, (5,5)),
	cv2.blur(image, (7,7))])

cv2.imshow("averaged blurr", blurred)
cv2.waitKey(0)

#gaussian blurring
	# like Average blurring, but uses a weighted mean
	# pixels around the central point will be given more weightage
	# the third parameter in cv2.GaussianBlurr is Sigma, which is standard deviation. here it is 0, so cv2 calculates the standard deviation
blurred = np.hstack([
	cv2.GaussianBlur(image, (3,3), 0),
	cv2.GaussianBlur(image, (5,5), 0),
	cv2.GaussianBlur(image, (7,7), 0)])

cv2.imshow("Gaussian blurr", blurred)
cv2.waitKey(0)

#median blurring
	# Most effective. Removes the salt and pepper noise. 
	# think of salt and pepper as if real salt and pepper is sprinkled over 
	# a real pic. Its a distraction, - a noise. Median blurring removes such granular noise.
	# median is the median of the neighbourhood. So it is more efficient.
	# for medianblur we dont need to provide 2 values, since we provide only the median
blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])

cv2.imshow("Median blurr", blurred)
cv2.waitKey(0)

#bilateral blurring
	# Makes the edge of image clear and crisp. The edges of the subject will be preserved. 
	# takes more time compared to others
	# like medianBlur the kernal size needs only 1 value as it uses the median
	# the 3rd parameter are color sigma- color medium. 
		# as the value of color sigma increases more colors will be included for blurring
	#the 4th parameter is the space sigma. As the space size increases more surrounding pixels furhter from the central pized will influence the blurring effect with its calculation, as long as the colors are similar
blurred = np.hstack([
	cv2.bilateralFilter(image, 3, 21, 21),
	cv2.bilateralFilter(image, 5, 31, 31),
	cv2.bilateralFilter(image, 7, 41, 41)])

cv2.imshow("bilateral blurr", blurred)
cv2.waitKey(0)
