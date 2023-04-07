/*
 * @lc app=leetcode.cn id=1144 lang=cpp
 *
 * [1144] 递减元素使数组呈锯齿状
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int movesToMakeZigzag(vector<int> &nums)
    {
        int a = 0, b = 0;
        for (int i = 1; i < nums.size(); i += 2)
        {
            a += max(0, nums[i] - min((i == 0) ? 1010 : nums[i - 1], (i == nums.size() - 1) ? 1010 : nums[i + 1]) + 1);
        }
        for (int i = 0; i < nums.size(); i += 2)
        {
            b += max(0, nums[i] - min((i == 0) ? 1010 : nums[i - 1], (i == nums.size() - 1) ? 1010 : nums[i + 1]) + 1);
        }
        return min(a, b);
    }
};
// @lc code=end
