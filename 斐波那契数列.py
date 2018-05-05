# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # 计算出前n项并保存，最后输出res中最后一项，注意这里n从0开始
        res = [0,1]
        while len(res) <= n :
            res.append(res[-1] + res[-2])
        return res[n]