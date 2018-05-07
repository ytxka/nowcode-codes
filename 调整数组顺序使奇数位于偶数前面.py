# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # 遍历list，分别将奇数和偶数添加到两个list中即可
        # 开始试图用for i in array,if为偶数remove i，然后array.append(i)的错误方法，
        # 后才发现此时移动一个元素之后list中元素索引已改变，故会得出错误结果
        odd, even = [], []
        for i in array:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return odd + even