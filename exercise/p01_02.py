# 在所有7位01串中，同时含有"101"串和"11"串的有多少个
from itertools import permutations

MAX = 127
str1 = "101"
str2 = "11"


class Solution():
    def __init__(self, string_length):
        self.string_length = string_length
        self.bins = []
        self.counts = 0

    def genStr(self, m):
        for dec in range(0, m + 1):
            self.bins.append(str(bin(dec))[2:])

    def calCounts(self, *args):
        for item in self.bins:
            flag = 1
            for arg in args:
                if arg not in item:
                    flag = 0
                    break
            if flag:
                self.counts += 1
        return self.counts


def main():
    s = Solution(7)
    s.genStr(MAX)
    result = s.calCounts(str1, str2)
    print(result)


if __name__ == '__main__':
    main()
