import os
from os import listdir, getcwd
wd=getcwd()
image_path=os.path.join(wd,'images')
files_name=os.listdir(image_path)
#print(files_name)

for i in files_name:
  file_name,extension=os.path.splitext(i)
  #print(extension)
  image=os.path.join(image_path,i)
  if (extension=='.jpg' or extension=='.JPG' or extension=='.jpeg' or extension=='.JPEG'):
    new_name=os.path.join(image_path,file_name+'_2_google'+'.jpg')
    os.rename(image,new_name)
    print('rename:\n',image,'--> \n',new_name)
  else:
    os.remove(image)
    print('remove:',image)
