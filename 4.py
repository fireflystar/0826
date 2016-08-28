#coding=utf-8

#水仙花数
l = range(0,10)

s = [(x,y,z)for x in l for y in l for z in l if (x**3+y**3+z**3==x*100+y*10+z) and (x!=0)]
print s


#九九乘法表的一般写法
i = 1
while i <= 9:
	j = 1
	while j <= i:
		print "%d*%d=%d" % (j, i, i*j),
		j += 1
	print '\n'
	i += 1


print '\n'*3

#九九乘法表的另类写法
i = 1
while i <= 9:
	j = 1
	while j <= 9:
		if j<i:
			print "     ",
		else:
			print "%d*%d=%d " % (i, j, i*j),
		j += 1
	print '\n'
	i += 1


#查找字符串里的字串,循环部分可以写成一个函数，但是有更好的函数find()
s = 'hejeapllo jeapedu.comjeapjeap'
sep = 'jeap'

i = 0
while i < len(s)- len(sep) + 1:
	if (s[i] == sep[0]) and (s[i:i + len(sep)] ==sep):
		print i,
	i += 1



