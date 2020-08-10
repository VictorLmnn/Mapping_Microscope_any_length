import cv2 as cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import time

master = tk.Tk()


def input ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=master, initialdir=currdir, title='Please select a directory')
    return tempdir
# def input():
#     input_path = tk.filedialog.askdirectory()
#     input_entry.delete(1, tk.END)  # Remove current text in entry
#     input_entry.insert(0, input_path)  # Insert the 'path'

def fullimage_merge ():

    image_path_list = []

    imageDir = input()
    #create a list all files in directory and
    #append files with a vaild extention to image_path_list
    for file in os.listdir(imageDir):
        extension = os.path.splitext(file)[1]
        image_path_list.append(os.path.join(imageDir, file))

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


    def concat_tile(im_list_2d):
        return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])
        
    timestr = time.strftime("%Y%m%d-%H%M%S")
    fullimage = concat_tile(null1)
    cv2.imwrite(str(timestr)+'.jpg', fullimage)
    cv2.imshow(str(timestr)+".jpg",fullimage)
    cv2.waitKey()
    # plt.imshow(fullimage)
    # plt.show()


top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Search for folder with seperate images:")
browse = tk.Button(top_frame, text="Browse", command=fullimage_merge)


top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
browse.pack(pady=5)

master.mainloop()