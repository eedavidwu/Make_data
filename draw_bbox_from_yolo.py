import os
from os import listdir, getcwd
from os.path import join
from PIL import Image

wd = getcwd()


def Crop_Worker(image, bboxes=None, out_image_folder=None, out_label_folder=None):
    img_file = os.path.join(wd, 'images', image)
    img=Image.open(img_file)
    file_name,extension=os.path.splitext(image)
    count=0
    for bbox in bboxes:
        if bbox[0]=='0':
            conf = '0 0'
        if bbox[0] == '1':
            conf = '0 1'
        if bbox[0] == '2':
            conf = '1 0'
        if bbox[0] == '3':
            conf = '1 1'
        count=count+1
        out_img_path = os.path.join(out_image_folder, file_name + '_worker'+ str(count)+ '.jpg')
        out_label_path=out_img_path.replace('.jpg','.txt').replace('worker_image','worker_labels')
        worker_file_name,extension=os.path.splitext(out_img_path)
        worker = img.crop((bbox[1], bbox[2], bbox[3], bbox[4])).save(out_img_path)
        label_file=open(out_label_path,'w')
        label_file.write(conf)
        label_file.close()

        Net_label_file = open('./test_labels.txt', 'a')
        Net_label_file.write(file_name + '_worker'+ str(count)+ '.jpg'+ ' ' + conf + '\n')
        Net_label_file.close()
    print('Complete:',image,'with',count,'workers')


def draw_all_bboxes(pic_folder, bboxes_txt, out_image_folder,out_label_folder):
    image_file_list=os.listdir(pic_folder)
    for image in image_file_list:
        #print(image)
        image_path=os.path.join(wd,'images',image)
        img = Image.open(image_path)
        w = img.size[0]
        h = img.size[1]

        anno_path=image_path.replace('images','anno').replace('.jpg','.txt')
        anno_file=open(anno_path,'r')
        lines=anno_file.readlines()
        bbox_img=[]
        for line in lines:
            line=line.split()
            attribute=line[0]
            x_c=int(float(line[1])*w)
            #print(x_c)
            y_c=int(float(line[2])*h)
            w_obj=int(float(line[3])*w)
            h_obj=int(float(line[4])*h)

            x_1=int(x_c-w_obj/2)
            x_2=int(x_c+w_obj/2)
            y_1=int(y_c-h_obj/2)
            y_2=int(y_c+h_obj/2)

            bbox=[attribute,x_1, y_1, x_2, y_2]
            bbox_img.append(bbox)

            #print(attribute)
            #print(bbox_img)
        Crop_Worker(image, bbox_img,out_image_folder,out_label_folder)



if __name__ == "__main__":
    #img_file = "./images/000001_1_google.jpg"
    img_folder='./images/'
    out_image_folder = "./worker_image/"
    out_label_folder = './worker_labels/'
    draw_all_bboxes(img_folder, out_image_folder, out_image_folder,out_label_folder)
