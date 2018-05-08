# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return None
        elif not pHead1 or not pHead2:
            return pHead1 or pHead2
        else:
            # 定义一个合并后的链表，递归解决
            mergedHead = None
            if pHead1.val <= pHead2.val:
                mergedHead = pHead1
                mergedHead.next = self.Merge(pHead1.next, pHead2)
            else:
                mergedHead = pHead2
                mergedHead.next = self.Merge(pHead1, pHead2.next)
            return mergedHead