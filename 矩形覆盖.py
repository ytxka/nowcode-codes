# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # 矩阵有n列时，若第一次按竖排摆放，则剩下f(n-1)种方法；
        # 第一次横排摆放，则剩下f(n-2)种方法。综上，依旧为斐波那契数列.
        res = [0,1,2]
        while len(res) <= number:
            res.append(res[-1] + res[-2])
        return res[number]