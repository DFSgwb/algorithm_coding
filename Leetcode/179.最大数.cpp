/*
 * @lc app=leetcode.cn id=179 lang=cpp
 *
 * [179] 最大数
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    static bool cmp(int a, int b)
    {
        string str_a = to_string(a);
        string str_b = to_string(b);
        return str_a + str_b > str_b + str_a;
    }
    string largestNumber(vector<int> &nums)
    {
        string res;
        sort(nums.begin(), nums.end(), cmp);
        for (auto num : nums)
        {
            if (!(num == 0 && res[0] == '0'))
                res += to_string(num);
        }
        return res;
    }
};
// @lc code=end
