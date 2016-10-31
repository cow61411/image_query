#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from numpy import array
import sift
from pylab import *
import os

datapath = "./../dataset"
imname = 'Penguins.jpg'
for dirs , root , files in os.walk(datapath):
	for filename in files:
		#im1 = array(Image.open(datapath + filename).convert('L'))
		name = filename.split(',')
		sift.process_image(filename,name[0] + '.sift')

		#l1,d1 = sift.read_features_from_file('Penguins.sift')

'''
figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()
'''
