'''
           爱奇艺2018秋季校招前端工程师（第二场），回文素数
  如果一个整数只能被1和自己整除,就称这个数是素数。
  如果一个数正着反着都是一样,就称为这个数是回文数。例如:6, 66, 606, 6666
  如果一个数字既是素数也是回文数,就称这个数是回文素数
  牛牛现在给定一个区间[L, R],希望你能求出在这个区间内有多少个回文素数。
'''
def main(l, r):
    if l <1 or r > 1000 or l > r:
        return 0
    flag = 0
    for i in range(l, r + 1):
        if isPrime(i) and isRound(i):
            flag += 1
    return flag

def isPrime(n):
    # 判断是否为素数。注意，1、0既不是素数也不是合数！
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True

def isRound(n):
    # 判断是否为回文数
    li = list(str(n))
    if li == li[::-1]:
        return True
    else:
        return False
  
l, r = map(int, input().split(' '))
res = main(l, r)
print(res)