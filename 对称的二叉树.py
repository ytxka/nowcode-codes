# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # 详细思路见《剑指offer》P159
        if not pRoot:
            return True
        return self.main(pRoot.left, pRoot.right)
    def main(self, rootL, rootR):
        if rootL == None and rootR == None:
            return True
        if rootL == None or rootR == None:
            return False
        if rootL.val != rootR.val:
            return False
        # 左子树的左子树 = 右子树的右子树 and 左子树的右子树 = 右子树的左子树
        return self.main(rootL.left, rootR.right) and \
                self.main(rootL.right, rootR.left)