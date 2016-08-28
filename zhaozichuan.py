#coding:utf-8
def get_sub(s, sub_head, sub_tail):
	sub_list = []
	print '进入子函数，查找以某某开头，以某某结尾的一系列子串'

	head = s.find(sub_head)
	tail = s.find(sub_tail, head)
	sub_list.append(s[head : tail+ len(sub_tail) ])
	
	while True:
		print '进入循环体'
		head = s.find(sub_head,tail)
		tail = s.find(sub_tail, head)
		print head ,tail
		if head != -1:
			sub_list.append(s[head : tail+ len(sub_tail) ])
			head = tail
		else:
			break

	return sub_list


s = 'welcom to visit my website http://www.baidu.com hehe! or\
 http://www.163.com or http://www.sohu.comalfjlasfjaswww.zhenghui.com'
sub_head = 'www'
sub_tail = '.com'
# head = s.find(sub_head)
# tail = s.find(sub_tail, head)
# print head,tail


# head = s.find(sub_head, tail)
# tail = s.find(sub_tail, head)
# print head,tail
print get_sub(s,sub_head,sub_tail)


