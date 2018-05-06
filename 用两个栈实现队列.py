# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # 用两个栈，A入队列，B出队列
        # 栈B为空时，A全部出栈到B，B再出栈（即出队列）
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()