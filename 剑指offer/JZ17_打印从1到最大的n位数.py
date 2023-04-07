from typing import List


class Solution:
    """
        输入数字n,按顺序打印出从1到最大的n位十进制数。比如输入3,则打印出 1、2、3一直到最大的3位数999。
    """
    def printNumbers(n: int) -> List[int]:
        return [i for i in range(1,10**n)]

if __name__ == '__main__':
    num=Solution.printNumbers(2)
    print(num)