#coding=utf-8
# leetcode 455
# 以下代码只ac了50%，或为数组越界
import sys

def dist(child, sugar, length):
	flag = 0
	for i in range(length):
		if sugar[i] >= child[i]:
			flag += 1
		else:
			break
	return flag

if __name__ == "__main__":
	arr = []
	for i in range(2):
		line = sys.stdin.readline().strip()
		values = list(map(int, line.split()))
		arr.append(values)
	if not arr or not arr[0] or not arr[1]:
		print(0)
	else:
		child = arr[0]
		sugar = arr[1]
		child.sort()
		sugar.sort()
		if max(sugar) < min(child):
			print(0)
		else:
			if len(child) >= len(sugar):
				res = dist(child, sugar, len(sugar))
			else:
				res = dist(child, sugar, len(child))
		print(res)