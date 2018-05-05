# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 左下角处元素向上递减向右递增，所以从左下角开始检查
        # 注意条件的判断必须用if...elif...else，而非3个if。因为if会逐一判断，可能造成数组越界！
        rows = len(array)
        cols = len(array[0])
        i = rows - 1
        j = 0
        while i >= 0 and j < cols:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                j += 1
            else :
                i -= 1
        return False