from typing_extensions import Self
from pip import main


class Solution:
    """
        给你一根长度为n的绳子,请把绳子剪成整数长的m段(m,n都是整数,n>1并且m>1,m<=n)
        每段绳子的长度记为k[1],...,k[m],请问k[1]*k[2]*...*k[m]可能的最大乘积是多少?
    """
    def cutRope(self, n:int) -> int:
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2,i):
                dp[i] = max(dp[i],max(j * (i - j), j * dp[i - j]))
        return dp[n]

if __name__ == '__main__':
    num=Solution.cutRope(8)
    print(num)