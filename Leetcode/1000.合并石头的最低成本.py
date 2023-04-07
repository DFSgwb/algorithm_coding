#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

# @lc code=start

from linecache import cache
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if n == 1:
            return 0
        S = [0]*(n+1)
        for i in range(len(stones)):
            S[i + 1] = S[i] + stones[i]
        @cache
        def dfs(left,right,div):
            if (right - left + 1) < div:
                return 10**9
            elif (right - left + 1) == div:
                return S[right+1] - S[left]
            # 还可以再细分
            if div == 1:
                return dfs(left,right,k) + S[right + 1] - S[left]
            ans = 10**9
            for i in range(left,right):
                ans = min(ans,dfs(left,i,1) + dfs(i+1,right,div - 1))
            return ans
        ans = dfs(0,n - 1,k)
        return ans if ans < 10**9 else -1
# @lc code=end