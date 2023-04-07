/*
 * @lc app=leetcode.cn id=1413 lang=cpp
 *
 * [1413] 逐步求和得到正数的最小值
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int minStartValue(vector<int> &nums)
    {
        // 也就是寻找nums前缀和中最小值
        int ans = 0;
        int res = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            res += nums[i];
            ans = min(res, ans);
        }
        return abs(ans) + 1;
    }
};
// @lc code=end
