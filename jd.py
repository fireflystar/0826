#coding:utf-8
import urllib
import urllib2



def get_sub(s, sub_head, sub_tail):
	sub_list = []
	print 'get_sub()函数 用于寻找某一页中符合某种特征的字符串'

	head = s.find(sub_head)
	tail = s.find(sub_tail, head)
	sub_list.append(s[head : tail+ len(sub_tail) ])
	

	while True:
		# print '进入循环体'
		head = s.find(sub_head,tail)
		tail = s.find(sub_tail, head)
		# print head ,tail
		if head != -1:
			sub_list.append(s[head : tail+ len(sub_tail) ])
			head = tail
		else:
			break

	sub_list = list(set( sub_list )) #去掉列表重复的元素
	return sub_list







def read(url):
	print ' read() 函数打开链接,   链接地址 >> 类文件 >> 大字符串'
	r = urllib2.urlopen(url)   #打开页面，得到类文件对象
	s = r.read()

	return s
	# urllib.urlretrieve(url,'1.txt')





#挖掘网页里的内容，怎么去除隐藏的用户名
def dig_net_page():
	pass








#翻到下一页，这里是一个难点,问问Python群里的，问问baidu
#Python 网页 翻页
def next_page():
	page_list = []
	#得到大字符串
	#大字符串里有 下一页，找到这个特征对应的链接
	#打开 这个链接，得到下一页的地址，并存入一个列表中
	#循环往复






def main():
	url = 'http://search.jd.com/Search?keyword=联想平板&enc=utf-8&pvid=0384rpri.f2v8fh'
	s = read(url)
	sub_list = get_sub(s,'item.jd.com/','.html')
	for i in sub_list:print i
	# for i in sub_list:
	# 	dig_net_page()





if __name__ == '__main__':
	main()
