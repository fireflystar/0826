#coding:utf-8

while True:
	reply = raw_input('请输入数字：')
	if reply == 'stop': break
	elif not reply.isdigit():
		print "Bad!" * 8
	else:
		if int(reply) < 20:
			print 'low'
		else:
			print int(reply) ** 2


# L = [1,2,3,4,5]
# while True:
# 	front, L = L[0], L[1:]
# 	print front, L

#工厂函数，函数返回函数会让python变得难懂
# map(函数，序列) 函数的参数个数决定了序列的数量
# map(int,'spam')
# filter 筛选	一个参数，一个序列
# >>> filter(lambda x: x%2 == 0,range(1,20))
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

# reduce 累乘 ，累加，累什么什么的。。。2个参数，一个序列
# >>> reduce(lambda x,y:x*y,range(1,10))  累乘
# 362880
# >>> reduce(lambda x,y:x+y,range(1,101))	累加
# 5050

# apply() 函数,  apply(function,(参数元祖))
# >>> def f(x,y,z):
# ...     return x+y+z
# ...
# >>> apply(f,(3,4,5))
# 12
# >>> f = lambda x,y,z:x+y+z
# >>> apply(f,(3,4,5))

