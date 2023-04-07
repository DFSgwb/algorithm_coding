/*
 * @lc app=leetcode.cn id=75 lang=cpp
 *
 * [75] 颜色分类
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    void sortColors(vector<int> &nums)
    {
        int zero = -1, two = nums.size();
        for (int i = 0; i < two; i++)
        {
            if (nums[i] == 0)
                swap(nums[++zero], nums[i]);
            else if (nums[i] == 2)
                swap(nums[--two], nums[i--]);
        }
    }
};
// @lc code=end
