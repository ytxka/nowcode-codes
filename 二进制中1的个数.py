# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        if n >= 0:
            return bin(n).count('1')
        else:
            # 求负数补码，（将对应正数的补码）取反再+1和-1再取反结果是一样的
            # 32-xxx，表示计算取反后1的个数（共有32位）
            num = abs(n)
            return 32 - (bin(num - 1)).count('1')