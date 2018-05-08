# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # 设置一个快指针一个慢指针，p2先走k-1步，然后p1和p2同时走，p2走到最后一个时，p1刚好指向倒数第k个
        if head == None or k < 1:
            return None
        p1 = p2 = head
        for i in range(k - 1):
            if p2.next != None:
                p2 = p2.next
            else:
                return None
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        return p1