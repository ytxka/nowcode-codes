# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # 遍历字符串即可
        res = ''
        for i in s:
            if i == ' ':
                res += '%20'
            else:
                res += i
        return res