#
# @lc app=leetcode.cn id=1547 lang=python3
#
# [1547] 切棍子的最小成本
#

# @lc code=start

from ast import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0]+cuts+[n]
        m = len(cuts)
        # 开辟一个m*m的二维数组
        dp = [[float('inf') for _ in range(m)] for _ in range(m)]
        for i in range(1,m):
            dp[i-1][i]=0
        """
        变量 m 代表初始的切割数目,cuts 数组表示初始切割位置,dp 数组用于记录最优切割的代价。
        1. 外层循环将枚举从后往前的所有区间长度,即 L = m-1, m-2, ..., 0。
        2. 内层循环将枚举所有可能的左右端点 L 和 R,其中 L < R。
        3. 再内部，通过枚举切割点 i,将区间 (L, R) 划分成 (L, i) 和 (i, R) 两个子区间。
        4. dp[L][R] 表示将区间 (L, R) 切割成最小的代价。我们可以从状态 dp[L][i] 和 dp[i][R]
        中得到两个子区间的最小代价,再加上当前这次切割的代价 cuts[R]-cuts[L],
        将它们加起来就得到了当前区间 (L, R) 的最小切割代价。
        5. 最终,dp[0][m] 即为所求解的最小切割代价。
        """
        for L in range(m-1, -1,-1):
            for R in range(L+1, m):
                for i in range(L+1,R):
                    dp[L][R] = min(dp[L][R], cuts[R]-cuts[L]+dp[L][i]+dp[i][R])
        return dp[0][m-1]       

# @lc code=end