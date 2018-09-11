# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # 开始和二叉树层序遍历按行输出相同
        # 再判断行数的奇偶决定是否翻转
        if not pRoot:
            return []
        tmpS = [pRoot]
        res = []
        while tmpS:
            nextS = []
            tmpRes = []
            for i in tmpS:
                tmpRes.append(i.val)
                if i.left:
                    nextS.append(i.left)
                if i.right:
                    nextS.append(i.right)
            tmpS = nextS
            res.append(tmpRes)
        # 以下为判断是否翻转
        result = []
        for key,val in enumerate(res):
            if key%2 == 0:
                result.append(val)
            else:
                result.append(val[::-1])
        return result
