# -*- coding:utf-8 -*-
class Solution:
    res = []
    def Permutation(self, ss):
        # 在本地测试通过，牛客网在线测试却有bug
        # 递归法实现。将字符串分为两部分，第一个字符head和后面其余字符
        # 将head和后面的每个字符交换，得到新的字符串；head位置向后移动1位，递归执行
        # 最后将结果去重（使用list转换为字典法去重，然后再转换为list）
        # sorted（ss）将ss转换为排序列表
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]
        ss = sorted(ss)
        self.work(ss,0)
        return sorted(list(set(self.res)))
    
    def work(self, ss, head):
        if head >= len(ss):
            newS = ''.join(ss)
            self.res.append(newS)
        else:
            for i in range(head, len(ss)):
                ss[head], ss[i] = ss[i], ss[head]
                self.work(ss, head + 1)
                # 下面这行代码的作用：将字符串复原，以便进行下一次换位
                ss[head], ss[i] = ss[i], ss[head]
                
# following is for test
# t = Solution()
# ss = 'abc'
# result = t.Permutation(ss)
# print(result)