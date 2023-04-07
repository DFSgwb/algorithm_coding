"""
    请你帮忙从1到n的数设计排列方案,使得所有的质数都应该被放在[质数索引]上,你需要返回可能的方案总数。
    由于答案可能会很大,所以返回的答案使用%10^9+7之后的结果
"""
from itertools import chain
from cv2 import sqrt
from sympy import isprime, re, sqf


class Solution:
    """
        将数分为两部分,一部分是质数,一部分是非质数,然后对两部分数分别进行全排列，
        将得到的结果进行相乘即可得到答案
    """
    def numPrimeArrangements(n) -> int:
        res1 = 0
        res2 = 0
        mod = int(1e9+7)
        for i in range(1,n+1):
            if isprime(i):
                res1 += 1
            else:
                res2 += 1
        ans = 1
        for i in chain(range(1, res1 + 1), range(1, res2 + 1)):
            ans = (ans * i) % mod
        return ans


    
    def isPrime(num):
        used = 2
        if num == 1:
            return False
        for i in range(2,int(sqrt(num)+1)):
            if num%i == 0:
                return False
        return True

if __name__ == "__main__":
    num = 5
    print(Solution.numPrimeArrangements(num))

