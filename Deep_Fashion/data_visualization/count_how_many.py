import os 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

FILE_ADDRESS = '/home/young-joo/Desktop/Cleaning_Complete/label_final.txt'

#MUST DO IT ACCORING TO THE NUMBER LABELS 
def count_num(file_address):
	our_file = open(file_address, 'r')
	our_file = our_file.read().splitlines()
	
	thick_cotton_sweater = 0 
	thin_cotton_sweater = 0 
	wool_sweater = 0 
	short_sleeve_top = 0 
	sleeveless_top = 0 

	jeans = 0 
	trousers = 0 
	leggings = 0 
	comfortable_pants = 0 
	shorts = 0 
	short_skirt = 0
	long_skirt = 0 

	long_full_body_wear = 0 
	short_full_body_wear = 0 

	cardigan = 0 
	blazer = 0 
	winter_wear = 0 
	 
	for counter in range(2, len(our_file), 1): 
		our_string = "".join(our_file[counter])
		our_string = our_string.split()
		label = our_string[1]
		if label == '1': 
			thick_cotton_sweater += 1
		elif label == '2': 
			thin_cotton_sweater += 1
		elif label == '3': 
			wool_sweater += 1
		elif label == '4': 
			short_sleeve_top += 1
		elif label == '5': 
			sleeveless_top += 1
			
		elif label == '6': 
			jeans += 1
		elif label == '7': 
			trousers += 1
		elif label == '8': 
			leggings += 1
		elif label == '9': 
			comfortable_pants += 1
		elif label == '10': 
			shorts += 1
		elif label == '11': 
			short_skirt += 1
		elif label == '12': 
			long_skirt += 1

		elif label == '13': 
			long_full_body_wear += 1
		elif label == '14': 
			short_full_body_wear += 1

		elif label == '15': 
			cardigan += 1
		elif label == '16': 
			blazer += 1
		elif label == '17': 
			winter_wear += 1

	print "there are %d images of thick cotton sweater\n" % thick_cotton_sweater
	print "there are %d images of thin cotton sweater\n" % thin_cotton_sweater
 	print "there are %d images of wool sweater\n" % wool_sweater  
 	print "there are %d images of short sleeve top\n" % short_sleeve_top  
	print "there are %d images of sleeveless top\n" % sleeveless_top
 
	print "there are %d images of jeans\n" % jeans  
	print "there are %d images of trousers\n" % trousers
	print "there are %d images of leggings\n" % leggings  
	print "there are %d images of comfortable pants\n" % comfortable_pants  
	print "there are %d images of shorts\n" % shorts  
	print "there are %d images of short_skirt\n" % short_skirt 
	print "there are %d images of long_skirt\n" % long_skirt

 	print "there are %d images of long full-body wear\n" % long_full_body_wear  
	print "there are %d images of short full-body wear\n" % short_full_body_wear  
	
	print "there are %d images of cardigan\n" % cardigan  
	print "there are %d images of blazer\n" % blazer  
	print "there are %d images of winter wear\n" % winter_wear  

	categories = range(1, 18)	
	y_pos = np.arange(len(categories))
	num_of_items = [thick_cotton_sweater, thin_cotton_sweater, wool_sweater, short_sleeve_top, sleeveless_top, jeans, trousers, leggings, comfortable_pants, shorts, short_skirt, long_skirt, long_full_body_wear, short_full_body_wear, cardigan, blazer, winter_wear] 
	plt.bar(y_pos, num_of_items, align='center', alpha=0.5)
	plt.xticks(y_pos, categories)
	plt.xlabel('Categories')
	plt.ylabel('Num of Items')
	plt.title('Num of Items in Each Category')
	
	plt.show()

count_num(FILE_ADDRESS)


