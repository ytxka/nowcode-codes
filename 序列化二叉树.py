# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.index = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)
    def Deserialize(self, s):
        # write code here
        li = s.split(',')
        self.index += 1
        if self.index >= len(s):
            return
        root = None
        if li[self.index] != '#':
            root = TreeNode(int(li[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

        