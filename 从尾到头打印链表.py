# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 法1：利用list.[::-1]实现list的反转
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        if listNode is None:
            return res
        while listNode is not None :
            res.append(listNode.val)
            listNode = listNode.next
        return res[::-1]

# 法2：递归
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]