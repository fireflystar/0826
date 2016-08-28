#coding:utf-8
import os,Image

def fileList(path):

	# print ">>>>",path,' '

	listofpath = os.listdir(path)
	for i in listofpath:
		pathnew = path + '/' + i
		if os.path.isdir(pathnew):
			pass	#假如是文件夹就什么都不做
		else:		
			im = Image.open(pathnew)
			(x,y) = im.size
			x_s = 480
			y_s = y * x_s/x
			out = im.resize((x_s, y_s),Image.ANTIALIAS)
			print (x_s, y_s)
			# out.save(path + '/' +i)
fileList("D:\upload\majia")