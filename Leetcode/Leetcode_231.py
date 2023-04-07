"""
    给你一个整数n,判断该整数是否是2的幂次方,如果是返回true,否则返回false
"""
from sympy import false, true


class Solution:
    # 直接位运算转二进制判断是否除了首位以外都是零即可
    def isPowerOfTwo(n:int)->bool:
        if n>0 and n&(n-1)==0:
            return true
        else:
            return false
        
if __name__ == "__main__":
    n=4
    print(Solution.isPowerOfTwo(n))

