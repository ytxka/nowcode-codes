# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # 递归求左右子树的深度，最后树的深度=左右子树中深度较大者+1
        if not pRoot:
            return 0
        if pRoot.left:
            hL = self.TreeDepth(pRoot.left)
        else:
            hL = 0
        if pRoot.right:
            hR = self.TreeDepth(pRoot.right)
        else:
            hR = 0
        return max(hL, hR) + 1