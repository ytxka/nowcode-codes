# 招行信用卡中心2018春招笔试题
# 给出一个非空的字符串，判断这个字符串是否是由它的一个子串进行多次首尾拼接构成的。
#例如，"abcabcabc"满足条件，因为它是由"abc"首尾拼接而成的，而"abcab"则不满足条件。
#思路：从最长的二等分开始查找，用等分后的子字符串拼接成新的字符串B，
#      与原字符串A进行比较，如果相等，返回这个字符串，
#      如果不相等进行三等分以此类推，如果直至n等分（n=字符串A长度）都不能满足，输出false
def main(s):
	if not s:
		return 'false'
	return find(s)
def find(s):
	if not s:
		return 'false'
	if len(S) == 1:
		return s
	flag = 2
	while len(s) / flag > 1:
		tmp = s[0:falg]
		if s == tmp * flag:
			return tmp
		else:
			flag += 1
	
	return 'false'

s = 'abcabc'
print(main(s))

