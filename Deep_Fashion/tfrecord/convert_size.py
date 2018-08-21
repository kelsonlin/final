import os
import itertools 
import cv2 as cv
import numpy as np  
import PIL 
from PIL import Image 

#PLEASE HAVE ALL THE FILES YOU NEED TOGETHER IN ONE FILE# 
#FILL IN THE PATH TO THE FOLDER THAT CONTAINS ALL OF YOUR FILES#
PATH_TO_FILES = '/home/waynelin/Desktop/'
SOURCE_PATH = '/home/waynelin/Desktop/'
DESTINATION_PATH = '/home/waynelin/Desktop/'
SIZE = 299
LABEL_FILE = PATH_TO_FILES + 'label.txt'

def convert_image(my_file): 
	addrs = list()
	our_file = open(my_file, 'r')
	our_file = our_file.read().splitlines()
	length = len(our_file) 
	for our in range(length):   
		our_string = "".join(our_file[our])
		our_string = our_string.split()
		addrs.append(our_string[0])
	for i in range(length):
		split = addrs[i].split(".jpg")
		img = Image.open(SOURCE_PATH+ addrs[i]) 
		img = img.resize((SIZE, SIZE), PIL.Image.ANTIALIAS) 
		img.save(DESTINATION_PATH+ split[0] + "revised.jpg")
		print "converted %d out of %d images" % (i + 1, length)
convert_image(LABEL_FILE)
