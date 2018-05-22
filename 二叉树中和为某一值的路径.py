# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        # 递归实现
        # 当时突然想到为何函数没有定义完的时候就可以递归调用自己，实际这种矛盾并不存在。
        if not root:
            return []
        elif root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        res = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for i in left + right:
        	# left、right、i都是list
            res.append([root.val] + i)
        return res


# 测试用例:{10,5,12,4,7},22

# 对应输出应该为:[[10,5,7],[10,12]]
