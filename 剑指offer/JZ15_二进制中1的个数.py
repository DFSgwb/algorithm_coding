from pip import main


class Solution:
    def __init__(self) -> None:
        pass
    """
        输入一个整数n,输出该数32位二进制表示中1的个数,其中负数用补码表示
    """
    """
        n&(n-1)会将n的二进制中最低位由1变成0:
            不断让当前的n与n-1做位与运算,直到n的二进制全部变为0停止,
            由于每次运算会使得n的最低位的1被翻转为0,因此运算次数就等于n的二进制位中1的个数
            也就是说位于运算次数就是1的个数
    """
    def NumberOf1(self, n:int)->int:
        cnt=0
        if n<0:
            n &= 0xffffffff
        while n!= 0:
            n = n&(n-1)
            cnt += 1
        return cnt

if __name__ == '__main__':
    num=Solution.NumberOf1(10)
    print(num)
