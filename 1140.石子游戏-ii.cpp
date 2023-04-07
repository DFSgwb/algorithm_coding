/*
 * @lc app=leetcode.cn id=1140 lang=cpp
 *
 * [1140] 石子游戏 II
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int stoneGameII(vector<int> &piles)
    {
        int s = 0, n = piles.size(), f[n][n + 1];
        for (int i = n - 1; i >= 0; --i)
        {
            s += piles[i];
            for (int m = 1; m <= i / 2 + 1; ++m)
            {
                if (i + m * 2 >= n)
                    f[i][m] = s;
                else
                {
                    int mn = INT_MAX;
                    for (int x = 1; x <= m * 2; ++x)
                        mn = min(mn, f[i + x][max(m, x)]);
                    f[i][m] = s - mn;
                }
            }
        }
        return f[0][1];
    }
};
// @lc code=end
