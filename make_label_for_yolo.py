import os
from os import listdir, getcwd
from os.path import join

wd = getcwd()
count=0
#For train images path:
image_folder_path=os.path.join(wd,'images')
image_file_list = os.listdir(image_folder_path)
num=len(image_file_list)
print ('Image:'+str(num))

anno_folder_path=os.path.join(wd,'anno')
anno_file_list = os.listdir(anno_folder_path)
num=len(anno_file_list)
print ('Anno:'+str(num))

label_folder_path=os.path.join(wd,'labels')
label_file_list = os.listdir(label_folder_path)
num=len(label_file_list)
print ('label:'+str(num))

for anno_file in anno_file_list:
  anno_path=os.path.join(anno_folder_path,anno_file)
  label_path=anno_path.replace('anno','labels')
  anno_file = open(anno_path, 'r')
  label_file = open(label_path, 'a')
  lines=anno_file.readlines()
  for line in lines:
    line=line.split()
    line='0'+' '+line[1]+' '+line[2]+' '+line[3]+' '+line[4]+'\n'
    label_file.write(line)
    #print(line)
    
  label_file.close()
