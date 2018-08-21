## Download from the Internet
##### We find new images by downloading images from google, yahoo, etc. And name the images as 1.jpg, 2.jpg, 3.jpg, ...

##### Then use labelImg: https://github.com/tzutalin/labelImg to generate corresponding xml files. You can type labelImg in the terminal after installation to open it. 
###### Usage Note: use shortcut keys to make this procedure faster: w key is for drawing, and ctrl-s is for saving.

##### The file generate_list.py will create the bbox.txt and the label.txt by iterating through all the images in the folder
###### Please specify NUM, which is the number of images in the folder
###### Please specify LABEL, which is the integer label of the category.
