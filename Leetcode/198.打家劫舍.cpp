/*
 * @lc app=leetcode.cn id=198 lang=cpp
 *
 * [198] 打家劫舍
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int rob(vector<int> &nums)
    {
        // 递归搜索+DP
        int n = nums.size();
        // 使用一个记忆数组缓存当前求到的部分结果
        // vector<int> cache(n + 2);
        // 只保存需要的前一个状态结果和前前一个状态的结果,使用滚动数组不断更新即可
        int f1 = 0, f0 = 0;
        for (int i = 0; i < n; ++i)
        {
            int new_res = max(f1, f0 + nums[i]);
            f0 = f1;
            f1 = new_res;
        }
        return f1;
    }
};
// @lc code=end
