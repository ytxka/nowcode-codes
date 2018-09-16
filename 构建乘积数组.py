# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # 基本方法，时间复杂度太高，不推荐
        if not A:
            return []
        B = []
        for i in range(len(A)):
            tmp = 1
            for j in range(len(A)):
                if j == i:
                    continue
                else:
                    tmp *= A[j]
            B.append(tmp)
        return B