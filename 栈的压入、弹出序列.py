# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # 设置一个辅助栈tmp，遍历压栈顺序，按压栈顺序入栈tmp
        # 当tmp栈顶等于弹出顺序popV[0]时，tmp出栈
        # 最后如果tmp不为空，则popV不是该栈的弹出顺序
        if not pushV or not popV or len(pushV) != len(popV):
            return False
        else:
            tmp = []
            for i in pushV:
                tmp.append(i)
                while tmp and tmp[-1] == popV[0]:
                    tmp.pop()
                    popV.pop(0)
            if tmp:
                return False
            return True