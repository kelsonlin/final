# Method 1 gives the freedom to move mislabeled images, while Method 2 will require you to remove the mislabeled images
#### Within the "img" folder, there are approximately 5000 folders with names containing the style and the category.
#### However, the organizing team may have mislabeled some of them. e.g. a Tank Top image is inside a Tee folder. 
#### In this case, you would want to move the Tank image to a correct folder.
#### So what I do is 
1. Create a folder named Sleeveless_Top and another named Short_Sleeved_Top
2. Say, I am now cleaning a folder named ACDC_Graphic_Tee, and I find that img_00000002.jpg should be categorized as Sleeveless_Top instead of Short_Sleeved_Top. 
3. I would create a folder in Sleeveless_Top named exactly the same as the original folder, which is ACDC_Graphic_Tee in this case. And move img_00000002.jpg to this folder. Hence now img_00000002.jpg has the path /Sleeveless_Top/ACDC_Graphic_Tee/img_00000002.jpg.
4. What if in ACDC_Graphic_Tee I find another image img_00000055.jpg that indeed is a Short_Sleeved_Top. I create a folder in Short_Sleeved_Top named ACDC_Graphic_Tee and put img_00000055.jpg to this folder. Hence now img_00000055.jpg has the path /Short_Sleeved_Top/ACDC_Graphic_Tee/img_00000055.jpg

#### After the images are organized in the correct folder, we can automate the process of generating text files by using get_lists.py

###### Please specify the path to each folders
###### Please specify the desired number of training images 
###### This python script will iterate through the images and generate three files, which are respectively label.txt, bbox.txt, and partition.txt""
