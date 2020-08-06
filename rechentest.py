import cv2 as cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image

#image path and valid extensions
imageDir = "Bilder/" #specify your path here
image_path_list = []
 
#create a list all files in directory and
#append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    image_path_list.append(os.path.join(imageDir, file))


# print(image_path_list)
null = []
for image in image_path_list:
    null.append(cv2.imread(image))

i=-1

for image in image_path_list:
    i += 1
    null[i]=cv2.resize(cv2.imread(image), dsize=(0, 0), fx=0.2, fy=0.2)


print(int((len(null))**(.5)))