# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 22:45:21 2021

@author: prakh
"""
# Import Relevant Libraries
import cv2
import numpy as np
###################################################################################
# Task 1 : Transform the image in the +x direction by 25%, and create an image
image = cv2.imread('images.jpg')
height, width = image.shape[:2]

M = np.float32([
	[1, 0, width/4],
	[0, 1, 0]
])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('shifted',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('task1.jpg', shifted)

###################################################################################
# Task 2 : Transform the image in the +y direction by 25%, and create an image
M = np.float32([
	[1, 0, 0],
	[0, 1, -height/4]
])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow('shifted',shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('task2.jpg', shifted)

###################################################################################
# Task 3: Rotate the image in Z by 90 degree
rotatedimage = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE) # Using cv2.rotate() method,Using cv2.ROTATE_90_CLOCKWISE rotate by 90 degrees clockwise
cv2.imshow('rotated image', rotatedimage) # Displaying the image
cv2.waitKey(0)
cv2.imwrite('task3.jpg', rotatedimage)

###################################################################################
# Task 4 : Rotate the image in Z by -90 degree
rotatedimage2 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('rotated image', rotatedimage2) # Displaying the image
cv2.waitKey(0)
cv2.imwrite('task4.jpg', rotatedimage2)


###################################################################################
# Task 5 : From the center of the image, in all directions, increase the RGB values of the pixels in a manner that, each pixel from the center, the percentage drops by 1%. i.e. the center pixel's RGB will increase by 50%, and the next pixels in x and y directions will be 49%. This goes on and on until the increase becomes 0 %.
image = cv2.imread('images.jpg')
image2 = image
image2 = image2.astype('float64')
height, width = image2.shape[:2]
height,width = height//2,width//2
image2[height,width] = image2[height,width]  + 0.5*image2[height,width] 

for i in range(1,height//2):
    for j in range(1,width//2):
        diff = max(i,j)
        image2[height-i,width-j] = image2[height-i,width-j] + (0.5 - 0.01*diff)*image2[height-i,width-j]
        image2[height-i,width+j] = image2[height-i,width+j] + (0.5 - 0.01*diff)*image2[height-i,width+j]
        image2[height+i,width-j] = image2[height+i,width-j] + (0.5 - 0.01*diff)*image2[height+i,width-j]
        image2[height+i,width+j] = image2[height+i,width+j] + (0.5 - 0.01*diff)*image2[height+i,width+j]

image2 = np.clip(image2,0,255).astype('uint8')
cv2.imshow('changed',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('task5.jpg', image2)



