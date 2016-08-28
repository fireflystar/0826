#coding:utf-8
#提取网址
# s = 'welcom to visit my website http://www.baidu.com hehe! or\
#  http://www.163.com or http://www.sohu.com'
# head = 'www'
# tail = '.com'

# i = 0
# while i < len(s):
# 	if (s[i] == head[0]) and (s[i:i + len(head)] == head):
# 		print i,
# 	i += 1
# print '\n'

# j = 0
# while j < len(s):
# 	if (s[j] == tail[0]) and (s[j:j + len(tail)] == tail):
# 		print j,
# 	j += 1

s = 'welcom to visit my website http://www.baidu.com hehe! or\
 http://www.163.com or http://www.sohu.comalfjlasfjaswww.zhenghui.com'
head = 'www'
tail = '.com'

# i = 0
# while i < len(s):
# 	if (s[i] == head[0]) and (s[i:i + len(head)] == head):
# 		# print i,    #找到开头
# 		j = i  #从开头的位置找结尾
# 		while j < len(s):
# 			if (s[j] == tail[0]) and (s[j:j + len(tail)] == tail):
# 				# print j,  #找到结尾
# 				break	#找到了结尾就退出，不在继续循环
# 			j += 1
# 		print s[i:j + len(tail)]
# 	i += 1


def dfind(s,head,tail):
	i = 0
	while i < len(s):
		if (s[i] == head[0]) and (s[i: i + len(head)] == head):
			j = i  
			while j < len(s):
				if (s[j] == tail[0]) and (s[j : j + len(tail)] == tail):
					break
				j += 1
			print s[i:j + len(tail)]
		i += 1

dfind(s,head,tail)
#如果用正则表达式可以更简洁的解决上面的问题