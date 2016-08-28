#coding:utf-8
#删除字符串里的字串

s = 'helxixxixlxxo jeapxixedu.com'
sub = 'xix'


i = 0
while i < len(s) - len(sub):
	if (s[i] == sub[0]) and (s[i: i + len(sub)] == sub):
		s = s[0:i] + s[i + len(sub):]
		i -= 1 #这行很关键哦
	i += 1

print s