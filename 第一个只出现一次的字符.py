def FirstNotRepeatingChar(s):
        # python字典版，本地通过在线有误
        if not s:
            return -1
        tmp = {}
        for i in s:
            if i not in tmp:
                tmp[i] = s.index(i)
            else:
                del tmp[i]
        print(tmp)
        return list(tmp.values())[0]

# print(FirstNotRepeatingChar('yantingya'))


class Solution:
    def FirstNotRepeatingChar(self, s):
        # 利用内置函数的简单版
        if not s:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1