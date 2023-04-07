"""
    假如有一排房子,共n个,每个房子可以被刷成红色,蓝色,绿色三种颜色中的一种,你需要粉刷所有的房子并且使其
    相邻的两个房子颜色不能相同,但是,市场上不同颜色油漆价格不同,所以房子粉刷成不同颜色的花费成本也是不一样的
    每个房子粉刷成不同颜色的花费是以一个nx3的正整数矩阵costs来表示的
    计算粉刷完所有房子最少的花费成本
"""
class Solution:
    def minCost(costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        明显是一道动态规划题型,使用dp[i][j]表示第i+1个方块粉刷第j个颜色时,前i+1个方块的最小花费
        也就有递推公式：
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+cost[i][0]
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+cost[i][1]
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+cost[i][2]
        """
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        for c in range(3):
            dp[0][c] = costs[0][c]
        for i in range(1, n):
            dp[i][0]=min(dp[i-1][1],dp[i-1][2])+costs[i][0]
            dp[i][1]=min(dp[i-1][0],dp[i-1][2])+costs[i][1]
            dp[i][2]=min(dp[i-1][0],dp[i-1][1])+costs[i][2]
        res = min(dp[n-1])
        return res
    

if __name__ == '__main__':
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    #osts = [[7,6,2]]
    num=Solution.minCost(costs)
    print(num)