# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # 其实就是层序遍历；
        # 在层序遍历时，先把每一层的结点存入数组中，下一个结点再入队列
        if not pRoot:
            return [] 
        res = []
        tmpStack = [pRoot]
        while tmpStack:
            result = []
            nextStack = []
            for i in tmpStack:
                result.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            res.append(result)
            tmpStack = nextStack
        return res