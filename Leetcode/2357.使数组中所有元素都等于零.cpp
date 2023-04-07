/*
 * @lc app=leetcode.cn id=2357 lang=cpp
 *
 * [2357] 使数组中所有元素都等于零
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int minimumOperations(vector<int> &nums)
    {
        // 等价于寻找有多少个不同的非零正整数
        unordered_set<int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] > 0)
            {
                hash.emplace(nums[i]);
            }
        }
        return hash.size();
    }
};
// @lc code=end
