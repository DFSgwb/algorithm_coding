#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1, n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return n-dp[0][n-1]
# @lc code=end