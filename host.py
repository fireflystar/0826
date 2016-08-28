#coding:utf-8
import os

class Domain():
	def __init__(self, domain, port, protocal):
		self.domain = domain
		self.port = port
		self.protocal = protocal
	def URL(self):
		if self.protocal == "https":
			URL = 'https://'+self.domain+':'+self.port+'/'
		if self.protocal == "http":
			URL = 'http://'+self.domain+':'+self.port+'/'
		return URL
	def lookup(self):
		os.system("host "+self.domain)