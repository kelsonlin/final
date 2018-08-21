import cv2 as cv

PATH_TO_FILES = '/home/young-joo/Desktop/Cleaning_Complete/'
TEXT_LOCATION_BBOX = PATH_TO_FILES + 'bbox.txt'

our_file = open(TEXT_LOCATION_BBOX, 'r')
our_file = our_file.readlines()
i = 1
for line in our_file:
	line = line.strip()
	line = line.split()
	image = cv.imread(PATH_TO_FILES + line[0])
	cv.rectangle(image, (int(line[1]),int(line[2])), (int(line[3]), int(line[4])), (0,0,255), 2)
	cv.imwrite(line[0] + '_bbox.jpg', image)
	i = i + 1
