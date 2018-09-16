# ac
import sys 
n = int(sys.stdin.readline().strip())

def main(n):
	arr = [1,1]
	for i in range(2, n + 2):
		arr.append(arr[i - 2] + arr[i - 1])
	return arr[n]

res = main(n)
print(res)
