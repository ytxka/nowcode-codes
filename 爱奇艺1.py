'''
   爱奇艺2019秋招，在线笔试练习题

   输入：输入数据有多组，每组占一行，由两个整数n（n<10000）和m(m<1000)组成，n和m的含义如前所述。
   输出：对于每组输入数据，输出该数列的和，每个测试实例占一行，要求精度保留2位小数。
   
   样例输入：81 4
             2 2
   样例输出：94.73
             3.41

'''

from functools import reduce

def sum(x, y):
		return x + y
while 1:
	n,m = map(int, input().split(' '))
	if n >= 10000 or m >= 1000 or m <= 0:
		break
	li = [n]
	for i in range(m - 1):
		li.append(li[i]**0.5)
	res = reduce(sum, li)
	print ('%.2f' %res)