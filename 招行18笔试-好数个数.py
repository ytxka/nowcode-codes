# 输入正整数n，求1-n中“好数”的个数
# 好数：将一个数字旋转180°后，若还是一个数字，且不等于旋转前的数字，则其为好数
# 比如输入n为10，则有4个好数（2、5、6、9）
import sys 
n = int(sys.stdin.readline().strip())

def main(n):
	if n <= 0:
		return
	if 0 < n <= 10:
		return 4
	if n > 10:
		flag = 0
		for i in range(11, n + 1):
			tmp = str(i)
			new = tmp
			if tmp.find('3')== 1 or tmp.find('4')==1 or tmp.find('7')==1:
				continue
			else:
				# print('tmp:'+tmp)
				if '2' in tmp:
					new = new.replace('2', '5')
				if '5' in tmp:
					new = tmp.replace('5', '2')
				if '6' in tmp:
					new = new.replace('6', '9')
				if '9' in tmp:
					new = new.replace('9', '6')
				if new[::-1] != tmp:
					flag += 1
				# print('new:'+new[::-1])

		return flag + 4

res = main(n)
print(res)
