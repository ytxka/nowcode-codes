# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # f(n) = 2*f(n-1)
        res = [1,2]
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            for i in range(number):
                res.append(2 * res[i + 1])
            return res[number - 1]