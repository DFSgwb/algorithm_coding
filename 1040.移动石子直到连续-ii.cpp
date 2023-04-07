/*
 * @lc app=leetcode.cn id=1040 lang=cpp
 *
 * [1040] 移动石子直到连续 II
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> numMovesStonesII(vector<int> &stones)
    {

        /*
        首先对石头的位置进行排序，然后计算最大移动次数。在石头连续的情况下，最大移动次数为
        stones[n-1]-stones[1]-n+2 或者 stones[n-2]-stones[0]-n+2，取两者中的最大值即可。
        接下来计算最小移动次数。可以考虑维护一个区间 [i, j]，使得该区间内的石头可以通过移动
        变成连续的。具体来说，如果 j + 1 < n 且 stones[j+1]-stones[i]+1 <= n，则可以将石头
        移动到 [stones[i]+1, stones[j+1]-1] 中的任意一个位置。此时，移动的代价为 n-(j-i+1)。
        如果 [i, j] 中只有 n-1 个石头且它们可以变成连续的，则需要额外移动两颗石头，代价为 2。
        遍历所有可能的区间 [i, j]，求出最小代价即可。
        最终返回最小和最大移动次数即可
        */
        int n = stones.size();
        sort(stones.begin(), stones.end());
        // 计算最大移动次数
        int max_moves = max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2);
        // 计算最小移动次数
        int i = 0, j = 0, min_moves = n;
        for (i = 0; i < n; i++)
        {
            while (j + 1 < n && stones[j + 1] - stones[i] + 1 <= n)
                j++;
            int cost = n - (j - i + 1);
            if (j - i + 1 == n - 1 && stones[j] - stones[i] + 1 == n - 1)
                cost = 2;
            min_moves = min(min_moves, cost);
        }
        return {min_moves, max_moves};
    }
};
// @lc code=end
