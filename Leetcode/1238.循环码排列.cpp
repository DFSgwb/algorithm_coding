/*
 * @lc app=leetcode.cn id=1238 lang=cpp
 *
 * [1238] 循环码排列
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> circularPermutation(int n, int start)
    {
        // 格雷码
        vector<int> ans(1 << n);
        for (int i = 0; i < 1 << n; ++i)
        {
            ans[i] = i ^ (i >> 1) ^ start;
        }
        return ans;
    }
};
// @lc code=end
