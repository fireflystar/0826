#coding:utf-8
import json
from sys import argv
import os
import urllib
import urllib2

def main(sub='',page=1):
	
	# 构建字符串
	sub = '棉服女'
	s1 = 'https://s.taobao.com/search?q=%s'
	s1 = s1 % sub
	s2 ='&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20160810&ie=utf8'
	s = s1 + s2

	# 打开页面分析
	# webpage_file = urllib.urlopen(s).read()
	webpage_file = urllib.urlretrieve(s,'1.txt')
	print webpage_file

