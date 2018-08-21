# There are 3 files in this folder
## convert_size.py: 
#### since every image is of different dimensions, we have to resize them. Resized images will be generated. 
###### Please specify a txt file, which can be either label.txt, bbox.txt, or partition.txt. The path will be extracted from each line. 
###### Please specify the SOURCE_PATH, the extracted path will be appended to this SOURCE_PATH to find the images.
###### Please specify the DESTINATION_PATH, the resized images will be generated under DESTINATION_PATH.
###### Please specify the hieght and width of the desired images.

## save_tfrecord.py: 
#### reads original images to get heights and widths to normalize bounding boxes then converts resized images to tfrecord. Hence both original images and resized images should be provided.
###### Please specify TEXT_LOCATION_LABEL, the txt file that categorizes the images.
###### Please specify TEXT_LOCATION_BBOX, the txt file that stores the bounding box information of each image.
###### Please specidy TEXT_LOCATION_CAT, the txt file that serves as a dictionary for correspondence of integer labels and actual label names.
###### Please specify TEXT_LOCATION_PARTIYION, the txt file that annotates which images are for training, testing, and validating.
###### Please specify the SIZE of the resized images.

## read_tfrecord.py: 
#### To check whether the tfrecord is generated correctly (if the labels and bounding boxes are not messed up, etc.), we read from the tfrecord and visualize them. matplotlib windows will pop out and show the results.
###### please specify BATCH_SIZE, which is the number of images that will be displayed in one window.
###### please specify NUM_BATCH, which is the number of windows that will pop out.
###### please specify SIZE, which is the dimensions of the images that were written into tfrecord.
