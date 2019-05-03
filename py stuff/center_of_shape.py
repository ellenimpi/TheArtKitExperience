# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np

import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "artkit-d6193.firebaseapp.com",
  "databaseURL": "https://artkit-d6193.firebaseio.com/",
  "storageBucket": "artkit-d6193.appspot.com",
  "serviceAccount": "credentials.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
# as admin
storage.child("images/from_mobile.jpg").download("downloaded.jpg")
# as user
# storage.child("images/example.jpg").put("example2.jpg", user['idToken'])
 
# construct the argument parse and parse the arguments
image = cv2.imread("downloaded.jpg")

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# args = vars(ap.parse_args())
 
# # load the image, convert it to grayscale, blur it slightly,
# # and threshold it
# image = cv2.imread(args["image"])

# def inverte(imagem, name):
#     imagem = (255-imagem)
#     cv2.imwrite(name, imagem)
# cv2.imshow("image", image)
# cv2.waitKey(0)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_black = np.array([0,0,0])
upper_black = np.array([180,180,180])
# Threshold the HSV image to get only black colors
mask = cv2.inRange(hsv, lower_black, upper_black)


# cv2.imshow("mask", mask)
# cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#invert the gray image
gray = cv2.bitwise_not(mask)

#testing
# cv2.imshow("new thang", gray)
# cv2.waitKey(0)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image

# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# img2 = cv2.drawContours(image, contours, -1, (0,255,0), 3)


cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours and place corners into list

corner_list = []

for c in cnts:
	# compute the center of the contour

	M = cv2.moments(c)
	# cX = int(M['m10']/M['m00'])
	# cY = int(M['m01']/M['m00'])
	# print(M['m10'])
	# print(cv2.contourArea(c))
	if M['m00'] != 0 and cv2.contourArea(c) > 10000:
		#might have to figure out what orientation the squares are in ******************************
		cX = int(M['m10']/cv2.contourArea(c))
		cY = int(M['m01']/cv2.contourArea(c))
		# print(cX)
		# print(cY)
		# draw the contour and center of the shape on the image
		corner_list.append([cX, cY])

		#testing corners, can comment out later
		# cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
		# cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
		# cv2.putText(image, "center", (cX - 20, cY - 20),
		# cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


		# show the image
		# cv2.imshow("Image", image)	
		# cv2.waitKey(0)

#draw picture based on square (person must be looking head on)
#add in trapezoid later
a = corner_list[3]
# print(a)
b = corner_list[2]
# print(b)
c = corner_list[0]
# print(c)
d = corner_list[1]
# print(d)
#now in z formation
storage.child("images/art_piece.jpg").download("art_piece.jpg")
image_to_show = cv2.imread("art_piece.jpg")
x_distance = int(((b[0] - a[0]) + (d[0] - c[0])) /2)
y_distance = int(((c[1] - a[1]) + (d[1] - b[1])) /2)
# r = x_distance / image.shape[1]
# dim = (x_distance, int(image.shape[0] * r))
# perform the actual resizing of the image and show it
resized = cv2.resize(image_to_show, (x_distance, y_distance))
# cv2.imshow("resized", resized)
# cv2.imshow("Image", image)
x_offset=a[0]
y_offset=a[1]
#this is a loop, i think
image[y_offset:y_offset+resized.shape[0], x_offset:x_offset+resized.shape[1]] = resized
cv2.imshow("image", image)
cv2.imwrite("to_mobile.jpg", image)
storage.child("images/to_mobile.jpg").put("to_mobile.jpg")
cv2.waitKey(0)


