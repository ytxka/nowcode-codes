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

