#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os, sys, pdb, numpy
from PIL import Image, ImageChops, ImageOps, ImageDraw

from os import listdir, getcwd

import shutil

wd=getcwd()
input_image_path=os.path.join(wd,'images')
input_label_path=os.path.join(wd,'labels')

output_path=os.path.join(wd,'out_images')
out_label_path=os.path.join(wd,'out_labels')
out_label=('./train_labels.txt')


if __name__ == "__main__":
  file_name = [name for name in os.listdir(input_image_path) if os.path.isfile(os.path.join(input_image_path, name))]
  label_out_file = open(out_label, 'w')
  print(len(file_name))
  for k in file_name:
    img_input = os.path.join(input_image_path,k)
    label_input=img_input.replace('images','labels').replace('.jpg','.txt')
    label=open(label_input).readline()

    label_out_file.write(k+' '+label+'\n')
  label_out_file.close()
