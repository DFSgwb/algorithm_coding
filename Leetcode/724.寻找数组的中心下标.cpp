/*
 * @lc app=leetcode.cn id=724 lang=cpp
 *
 * [724] 寻找数组的中心下标
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int sum = 0;
        int tmp = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            sum += nums[i];
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (tmp * 2 + nums[i] == sum)
                return i;
            tmp += nums[i];
        }
        return -1;
    }
};
// @lc code=end
