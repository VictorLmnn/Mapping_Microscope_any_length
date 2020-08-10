import cv2 as cv2
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    return tempdir

def input():
    input_path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'



top_frame = tk.Frame(root)
bottom_frame = tk.Frame(root)
line = tk.Frame(root, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input Folder Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

fullimage_name = tk.Label(bottom_frame, text="Fullimage Name")
output_entry = tk.Entry(bottom_frame, text="", width=40)


begin_button = tk.Button(bottom_frame, text='Begin!')

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

fullimage_name.pack(pady=5)
output_entry.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)


root.mainloop()