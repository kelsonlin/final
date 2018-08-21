import os
import dict_categories as d
PATH = '/home/waynelin/Desktop/fashion/data/cleaned_img/'
TRAIN_SIZE=2900
####This function iterates through the images in a folder and writes the corredponding integer label
#### accroding to the dict_categories, which reads in the list_category_cloth.txt
def get_list(directory, cat_name, result_f):
        for dirname in os.listdir(directory):
            print dirname 
            for filename in os.listdir(directory+'/'+dirname):
                if ".jpg" in filename:
                    result_f.write("img/"+dirname+"/"+filename)
                    result_f.write("\t\t\t"+str(d.after[cat_name])+'\n')
#### This function iterates through the bounding box file and find the corresponding bbox information 
#### NOTE: this function requires extra time since it has a complexity of O(n^2)
def gen_bbox_list(img, bbox_lines, result_f):
    for line in bbox_lines:
        if img in line:
            result_f.write(line+'\n')
#### This function generates the partition.txt, it assignes the first TRAIN_SIZE images as training images, 
#### and the rest as testing images
def gen_part_list(label_lines, result_f, target):
    counter = 0
    for label_line in label_lines:
        if counter %2000 ==0:
            print counter
        label_line = label_line.split()
        if d.after[target] == label_line[1]:
            if counter < TRAIN_SIZE:
                result_f.write(label_line[0]+'\t\t\t\t'+"train\n")
            else:
                result_f.write(label_line[0]+'\t\t\t\t'+"test\n")
            counter += 1


if __name__=="__main__":
    with open("new_label.txt", "a") as result_f:
        get_list(PATH+'Jacket_incomplete/', "Winter_Wear", result_f)
        get_list(PATH+'Tank_incomplete/', "Sleeveless_Top", result_f)
        get_list(PATH+'Tee_incomplete/', "Short_Sleeve_Top", result_f)
        get_list(PATH+'Wool_Sweater/', "Wool_Sweater", result_f)
    with open("new_label.txt", 'r') as label_f:
        label_lines = label_f.read().splitlines()
        with open("list_bbox.txt", 'r') as bbox_f:
            bbox_lines = bbox_f.read().splitlines()
            with open("new_bbox.txt", "a") as result_f:
                for label_line in label_lines:
                    label_line =label_line.split()
                    print label_line[0] 
                    gen_bbox_list(label_line[0],bbox_lines, result_f)

    with open("new_label.txt", 'r') as label_f:
        label_lines = label_f.read().splitlines()
        with open("new_part.txt", 'a') as result_f:
            gen_part_list(label_lines, result_f, "Winter_Wear")
            gen_part_list(label_lines, result_f, "Sleeveless_Top")
            gen_part_list(label_lines, result_f, "Short_Sleeve_Top")
            gen_part_list(label_lines, result_f, "Wool_Sweater")
            








