# 给出一个整数n，将n分解为至少两个整数之和，使得这些整数的乘积最大化，
# 输出能够获得的最大的乘积。例如：2=1+1，输出1；10=3+3+4，输出36。
# 招行信用卡中心笔试题，注意oj时，raw_input返回结果为字符串，需转换为数字！

def main(x):
	if x < 2:
		return
	if x == 2:
		return 1
	if x == 3:
		return 3
	if x == 4:
		return 4
	flag = 1
	while x > 4:
		x -= 3
		flag *= 3
	return flag * x

print(main(10))
