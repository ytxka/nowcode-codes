# -*- coding:utf-8 -*-
class Solution:
	# 方法1：直接求解，运行时间高些(23ms 5728k)
    def Power(self, base, exponent):
        return base ** exponent

    # 方法2：分类讨论再求解（排行榜里面运行时间<1ms，然而自己运行没有差多少...
    def Power(self, base, exponent):
        if base == 0:
            return 0
        elif base == 1:
            return 1
        elif exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            return pow(base, exponent)