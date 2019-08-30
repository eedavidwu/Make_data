import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

wd = getcwd()

#For train images path:
worker_bbox_results=os.path.join(wd,'comp4_det_test_person.txt')
save_path=os.path.join(wd,'worker_coco')

results=open(worker_bbox_results).readlines()
i=0
for line in results:
    #i=i+1
    line=line.split(' ')
    file_name=line[0]+'.jpg'
    file_path=os.path.join(wd,'images',file_name)
    if (float(line[1])>0.98):
        x1=int(float(line[2]))
        x2=int(float(line[4]))
        y1=int(float(line[3]))
        y2=int(float(line[5]))
        i=i+1
        img=Image.open(file_path)
        worker=img.crop((int(x1),int(y1),int(x2),int(y2)))
        worker.save(os.path.join(save_path,('worker_'+str(i)+'_'+file_name)))
        print(img.size)
        print(file_name,x1,x2,y1,y2)
        print(worker.size)

print('all number:',i)

    #img=Image.open(file_path)
    #print(img.size)
