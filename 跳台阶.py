# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        # 对于第n个台阶来说，只能从n-1或者n-2的台阶跳上来
        # 所以F(n)=F(n-1)+F(n-2)，斐波那契数列
        # F(1)=1，F(2)=2
        if number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            res = [1,2]
            for i in range(number):
                res.append(res[i] + res[i+1])
            return res[number-1]