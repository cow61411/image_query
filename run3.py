import os
from PIL import Image
import sift
from scipy.cluster.vq import vq , kmeans , whiten
import numpy
import math
from pylab import *

datapath = "./../dataset/"


def cal(queryname , judge):
	features = {}
	i = 0
	model = zeros(128)
	for dirs , root , files in os.walk(datapath):
		for filename in files:
                        #sift.process_image(datapath + filename , './sifts/' + filename[:-4] + '.sift')
                        
                        l , d = sift.read_features_from_file('./sifts/' + filename[:-4] +'.sift')
			features[filename] = d
			i += 1
			for i in range(len(d)):
				model = vstack((model , d[i]))

	model = delete(model , 0 , 0)

	query = zeros(128)
	sift.process_image(datapath + queryname , 'temp.sift')
	l , d = sift.read_features_from_file('temp.sift')

	for i in range(len(d)):
		query = vstack((query , d[i]))
	query = delete(query , 0 , 0)

	whitened = whiten(model)
	k , num = kmeans(whitened , 10)

	queryarr , disnum = vq(query , k)

	temp = [0] * 10
	for i in queryarr:
		temp[i] += 1


	countdict = {}
	for k , v in features.iteritems():
		countdict[k] = [0] * 10
		featurearr , desnum = vq(features[k] , k)
		for i in featurearr:
			countdict[k][i] += 1

	result = {}
	for k , v in countdict.iteritems():
		numsum = 0
		for i in range(10):
			val = countdict[k][i]
			numsum += (val - temp[i]) * (val - temp[i])
		result[k] = numsum

	result = sorted([(v , k) for (k , v) in result.items()] , reverse = False)
	if judge:
		for i in result[:10]:
			print i
	else:
		return result[:10]
