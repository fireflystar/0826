#coding:utf-8
def fib(n):
	a, b = (0, 1)
	while a < n:
		print a,
		a, b = b, a+b

def main():
	fib(20)

if __name__ == "__main__":
	main()
