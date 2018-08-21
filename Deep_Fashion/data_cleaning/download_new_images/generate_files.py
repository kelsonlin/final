import numpy as np 
import xml.etree.ElementTree as ET
NUM = 443
NUM+=1
LABEL = 2
#Should be the same directory as the img folder
PATH_TO_TEXT_FILE = '/home/waynelin/Desktop/Trousers_01'

#initializing the tree 
tree = ET.parse('/home/waynelin/Desktop/Trousers_01/1.xml')
root = tree.getroot()

my_array = []
for i in range(1, NUM):
	my_array.append([]) 
	#initializing the tree 
	tree = ET.parse('/home/waynelin/Desktop/Trousers_01/%d.xml' % i)
	root = tree.getroot()
	num = i - 1  
	for coord in root.iter('bndbox'):
		counter_2 = 0 
		for elem in coord.iter():
			if counter_2 != 0: 
				my_array[num].append(elem.text)
			counter_2 += 1

#write everything into a text file
print my_array

#generating the bbox file 
donefile = open("/home/waynelin/Desktop/bbox_trousers.txt", "w")
i = 0 
for i in range(NUM-1): 
	xmin = my_array[i][0]
	ymin = my_array[i][1]
	xmax = my_array[i][2]
	ymax = my_array[i][3]
        #this is the line that is going to be written in the txt file
        #this should be the path to the image
	donefile.write(("img/Trousers_01/%d.jpg" % (i + 1)) + " " + xmin + " " + ymin + " " + xmax + " " + ymax + "\n") 
donefile.close()

#generating the label file 
donefile = open("/home/waynelin/Desktop/label_trousers.txt", "w") 
for i in range(1,NUM): 
        #this is the line that is going to be written in the txt file
        #this should be the path to the image
	donefile.write(("img/Trousers_01/%d.jpg" % i) + " " + str(LABEL)+ "\n") 
donefile.close() 

