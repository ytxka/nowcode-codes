# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # 魔方旋转法，每次取出第一行，然后逆时针旋转，重复取第一行
        # [::-1]的用法（翻转）
        # 此题有点难- -
        res = []
        while len(matrix) > 0:
            res.extend(matrix[0])
            matrix = zip(*matrix[1:])[::-1]
        return res