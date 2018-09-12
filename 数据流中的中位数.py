# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
    def Insert(self, num):
        # write code here
        self.arr.append(num)
        self.arr.sort()
    def GetMedian(self, data):
        # write code here
        length = len(self.arr)
        if length % 2 != 0:
            # // 表示整数除法， / 表示浮点除法
            return self.arr[length // 2]
        else:
            # python 2.x 中，int/int结果为int，所以最后要除以2.0而非2
            return (self.arr[(length) // 2] + self.arr[(length) // 2 - 1]) / 2.0