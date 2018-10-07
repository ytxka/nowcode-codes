# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return None
        if len(numbers) == 1:
            return numbers[0]
        tmp = {}
        flag = len(numbers) / 2.0
        for i in numbers:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
            if tmp[i] > flag:
                return i
        return 0