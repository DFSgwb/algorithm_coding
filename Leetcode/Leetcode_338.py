"""
    给你一个整数n,对于0<=i<=n中的每一个i,计算其二进制表示中的1的个数,返回一个长度为n+1的数组
    作为答案ans
"""
from typing import List
class Solution:
    """
        直接使用位运算
    """
    def numCount(num:int)->int:
        count = 0
        while num!=0:
            if num&1:
                count+=1
            num = num>>1
        return count
    """
        动态规划
    """
    def countBits(n:int)->List[int]:
        bits = [0]
        highBit = 0
        for i in range(1,n+1):
            if i&(i-1) == 0:
                highBit=i
            bits.append(bits[i-highBit]+1)
        return bits
    def countBits2(n:int)->List[int]:
        ans = []
        for i in range(0,n+1):
            ans.append(Solution.numCount(i))
        return ans
if __name__ == "__main__":
    n=5
    print(Solution.countBits(n))
    print(Solution.countBits2(n))
    
