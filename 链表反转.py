# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 循环法，pre指向前一个结点，phead为当前结点，每次使pHead.next = pre
        if not pHead or not pHead.next:
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next
            pHead.next = pre
            pre = pHead # 向后推进，对之后的每个结点做反转
            pHead = tmp
        return pre