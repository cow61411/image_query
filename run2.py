import os
from math import pow
from PIL import Image

datapath = "./../dataset/"

def cal(query , judge):
	rdes = {}
	gdes = {}
	bdes = {}
	for dirs , root , files in os.walk(datapath):
		for filename in files:
			image = Image.open(datapath + filename)
			rarg , garg , barg = CLD(image)
			rdes[filename] = rarg
			gdes[filename] = garg
			bdes[filename] = barg

	queryimage = Image.open(datapath + query)
	queryr , queryg , queryb = CLD(queryimage)

	result = {}
	for (k , v) in rdes.items():
		res = 0
		for (i , j) in enumerate(v):
			temprdes = rdes[k]
			tempgdes = gdes[k]
			tempbdes = bdes[k]
			tempr = (temprdes[i] - queryr[i]) ** 2
			tempg = (tempgdes[i] - queryg[i]) ** 2
			tempb = (tempbdes[i] - queryb[i]) ** 2
			tempr = pow(tempr , 0.5)
			tempg = pow(tempg , 0.5)
			tempb = pow(tempb , 0.5)
			res += tempr + tempg + tempb
		result[k] = res

	result = sorted([(v , k) for (k , v) in result.items()] , reverse = False)
	if judge:
		for i in result[:10]:
			print i
	else:
		return result[:10]
	
def CLD(image):
	width , height = image.size
	croph = height / 8
	cropw = width / 8
	resultr = []
	resultg = []
	resultb = []
	#print filename
	for h in range(8):
		for w in range(8):
			#print "%d   %d   \n" % (h , w)
			hstart = h * croph
			hend = (h + 1) * croph
			wstart = w * cropw
			wend = (w + 1) * cropw
			newimg = Image.new('RGB' , (cropw , croph) , 255)
			ranges = (wstart , hstart , wend , hend)
			newimg.paste(image.crop(ranges))
			tempr = 0
			tempg = 0
			tempb = 0
			
			pixel = newimg.load()
			for h in range(croph):
				for w in range(cropw):
					r , g , b = pixel[w , h]
					tempr += r
					tempg += g
					tempb += b
			tempr /= (w * h)
			tempg /= (w * h)
			tempb /= (w * h)
			resultr.append(tempr)
			resultg.append(tempg)
			resultb.append(tempb)

			return resultr , resultg , resultb

