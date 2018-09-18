# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # 分割为上下三角矩阵，详见剑指offer
        if not A:
            return []
        head = [1]
        tail = [1]
        for i in range(len(A)-1):
            head.append(A[i] * head[i])
            tail.append(A[-1 - i] * tail[i])
        return [head[j] * tail[-j-1] for j in range(len(head))]
            