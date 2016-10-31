import os
from PIL import Image
from numpy import array 
from math import sqrt

datapath = "./../dataset/"
#queryfile = "ukbench00000.jpg"

index = {}

def distance(query , indexes):
	total = 0
	#print len(query)
	#print len(indexes)
	for i in range(len(query)):
		total += (query[i] - indexes[i]) * (query[i] - indexes[i])
		#print i
	return sqrt(total)
			
def cal(name , judge):
	f = Image.open(datapath + name)
	queryindex = f.histogram()

	for dirs , root , files in os.walk(datapath) : 
		for filename in files:
			f = Image.open(datapath + filename)
			f = f.histogram()
			test = array(f)
			index[filename] = distance(queryindex , f)
			#print index[len(index) - 1]
			#print f

	result = sorted([(v , k) for (k , v) in index.items()] , reverse = False)

	if judge:
		for i in result[:10]:
			print i
	else:
		return result[:10]



