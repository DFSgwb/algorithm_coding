from sympy import re


class Solution:
    """
        输入一个整数n,输出斐波那契数列的第n项
        矩阵快速幂算法
    """
    def Fibonacci(self , n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return c