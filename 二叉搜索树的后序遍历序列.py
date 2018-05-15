# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 二叉搜索树的后序遍历，最后一个元素为root，前面必可以分为两部分
        # 一部分（左子树）小于root，一部分（右子树）大于root
        # 递归判断左右子树
        if not sequence:
            return False
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        index = 0
        while sequence[index] < root:
            index += 1
        # 下面这种for循环写法有误    
        # for i in sequence[:-1]:
        #     if i > root:
        #         index = sequence.index(i)
        #         break
        left = sequence[:index]
        right = sequence[index:-1]
        
        leftIs = True
        rightIs = True
        
        for j in right:
            if j < root:
                return False
        if left:
            leftIs = self.VerifySquenceOfBST(left)
        if right:
            rightIs = self.VerifySquenceOfBST(right)
        return leftIs and rightIs