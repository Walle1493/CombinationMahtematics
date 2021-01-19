# 1-6 组成 4位偶数，各位数字各异
# permutations生成全排列
from itertools import permutations


class Solution():
    # 初始化列表以及列表长度
    def __init__(self, lst, length):
        self.lst = lst
        self.length = length
        # 是否改为静态变量？
        self.n = 0
        self.m = 0

    # 生成self.lst的self.length排列
    # def genAllRange(self):
    #     return list(permutations(self.lst, self.length))

    # 计算n和m的值：n-符合条件的数的个数，m-总和
    def calnm(self):
        # 如何单独写这个函数？
        range_list = list(permutations(self.lst, self.length))
        for item in range_list:
            if item[-1] % 2 == 0:
                self.n += 1
                for i in range(1, self.length + 1):
                    self.m += item[-i] * (10 ** (i - 1))
        return self.n, self.m

    # 展示结果
    # def showResult(self):
    #     return self.n, self.m

    def showAllRange(self, range_list):
        for item in range_list:
            print(item)
        # print(len(range_list))


def main():
    inputs = list(range(1, 7))
    s = Solution(inputs, 4)
    result = s.calnm()
    print("n={}, m={}".format(*result))


if __name__ == '__main__':
    main()
