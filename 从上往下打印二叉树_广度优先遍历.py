# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # 此题即树的层序遍历（广度优先遍历）
        # 借助一个队列queue实现
        # 第一次将根节点入队列，然后出队列，保存root.val至res
        # 之后依次将左右子树入队列，重复添加val至res，知道队列为空
        if not root:
            return []
        else:
            queue = []
            res = []
            queue.append(root)
            while queue:
                node = queue.pop(0)
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return res