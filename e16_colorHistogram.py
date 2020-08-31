from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

#you may need to install python tkinter
#number of pixels in x axis and number of pixels(intensity) in yaxis


# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

# loading and converting the image into numpy array
image = cv2.imread(args["image"])


# split image to channels
chans = cv2.split(image)
print("the chans are/is: ",chans)
# set the tuple
colors= ("b","g","r")

plt.figure()
plt.title("Color Histogram")
plt.xlabel("The Bins")
plt.ylabel("Number of pixels")


# 1st param is image- it must be in a list, even if it is a single image.
# 2nd channels: index of channel to compute for histogram
    # grayscale is 0
    #for RGB the channel list will be [0,1,2]
#3rd is mask. If a mask is provided then histogram is calculated only for masked pixels
#4th- histogram size- the number of pixels to use when computing histogram
#5th- range of pixels, usually 0 to 256
for( chan, Color) in zip(chans,colors):
    #lets create the histogram
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlim([0, 256])


plt.show()

cv2.waitKey(0)