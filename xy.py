import numpy as np
import cv2
import csv

#import image
img = cv2.imread('task2_2.png')

#make mask
def mask(image):
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #RGB to HSV
    #setting threshold
    grade_min = np.array([0, 1, 1], np.uint8)
    grade_max = np.array([179, 255, 255], np.uint8)

    threshold_img = cv2.inRange(image_hsv, grade_min, grade_max) #binarization using threshold
    threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB) #HSV to RGB

    return(threshold_img)


img1 = mask(img)
#make binary image
imbinary = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imbinary, 15, 255, cv2.THRESH_BINARY)

#detect the edge of image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print("Number of Contours = "+ str(len(contours)))

for i in range(len(contours)):
    print(contours[i])  #print (x,y) of the edge

    #make csv file of (x,y) of the edge
    with open('xy3.csv', 'w') as file:
        for j in contours[i]:
            print(j[0])
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(j)

cv2.drawContours(img, contours, -1, (0, 255, 0), 3) #draw edge line
cv2.imshow('Image', img)
cv2.imshow('Image BINARY', imbinary)



cv2.waitKey(0)
cv2.destroyAllWindows()