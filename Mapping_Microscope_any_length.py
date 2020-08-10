import cv2 as cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image

#image path and valid extensions
imageDir = "#19850_40x40_klein" #specify your path here
image_path_list = []
 
#create a list all files in directory and
#append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    image_path_list.append(os.path.join(imageDir, file))


#print(image_path_list)
null = []
for image in image_path_list:
    null.append(cv2.imread(image))

i=-1

for image in image_path_list:
    i += 1
    null[i]=cv2.resize(cv2.imread(image), dsize=(0, 0), fx=0.2, fy=0.2)

null1 = []
for i in range(int((len(null))**(.5))):
    null1.append([])

    for j in range(int((len(null))**(.5))-1):
        null1[i].append(null[i*int((len(null))**(.5)) + j])


#print(null[0:1])
#im1 = cv2.imread('JLUunten.jpg')

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

#im1_s = cv2.resize(im1, dsize=(0, 0), fx=0.5, fy=0.5)

#basic example
# im_tile = concat_tile([[im1_s, im1_s, im1_s, im1_s],
#                        [im1_s, im1_s, im1_s, im1_s],
#                        [im1_s, im1_s, im1_s, im1_s]])
# cv2.imwrite('JLUleftright.jpg', im_tile)


#fullimage = concat_tile([null[0:17],null[17:34],null[34:51],null[51:68],null[68:85],null[85:102],null[102:119],null[119:136]])
fullimage = concat_tile(null1)
cv2.imwrite('fullimage_any_length.jpg', fullimage)
cv2.imshow("fullimage.jpg",fullimage)
cv2.waitKey()
# plt.imshow(fullimage)
# plt.show()
