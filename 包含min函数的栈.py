# -*- coding:utf-8 -*-
# solution one: 直接使用python的min()函数
class Solution:
    def __init__(self):
        self.res = []
    def push(self, node):
    	# write code here
        self.res.append(node)
    def pop(self):
        # write code here
        top = self.res.pop()
        return self.res
    def top(self):
        # write code here
        return self.res[-1]
    def min(self):
        # write code here
        return min(self.res)
        
# -*- coding:utf-8 -*-
# solution two：设置一个辅助栈tmp。tmp每次都入栈，如果node小于res栈顶元素，则res入栈
# 此时res[-1]一定是最小的
# 但tmp出栈后，也要确保res[-1]是tmp所有元素中最小的，
# 所以如果tmp.pop() == res[-1]，即tmp中要出栈的元素是最小元素，则将res也出栈，否则res不出栈
# 这样可以确保无论入栈出栈多少次，res[-1]永远为最小元素
class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
    def push(self, node):
        self.tmp.append(node)
        if not self.res or node < self.res[-1]:
            self.res.append(node)
    def pop(self):
        # write code here
        if self.tmp[-1] == self.res[-1]:  # 注意此句含义
            self.res.pop()
        self.tmp.pop()
    def top(self):
        # write code here
        return self.tmp[-1]
    def min(self):
        # write code here
        return self.res[-1]
        