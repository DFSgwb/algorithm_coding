"""
    给定一个严格递增的正整数数组形成的序列arr,找到arr中最长的
    斐波那契数列的子序列长度,如果不存在返回0
"""
from collections import defaultdict
from typing import List


class Solution:
    def lenLongestFibSubseq(arr:List[int])->int:
        n = len(arr)
        idx_map = {num : i for i,num in enumerate(arr)}
        ans = 0
        dp = defaultdict(lambda:defaultdict(lambda:2))
        for i in range(n-1):
            for j in range(i+1,n):
                next = arr[i]+arr[j]
                if next  in idx_map:
                    dp[j][idx_map[next]] = dp[i][j] + 1
                    ans = max(ans, dp[j][idx_map[next]])
        return ans


if __name__ == "__main__":
    arr = [1,3,7,11,12,14,18]
    print(Solution.lenLongestFibSubseq(arr))