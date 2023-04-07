/*
 * @lc app=leetcode.cn id=1017 lang=cpp
 *
 * [1017] 负二进制转换
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    string baseNeg2(int n)
    {
        if (n == 0)
            return "0";
        int k = 1;
        string ans;
        while (n)
        {
            if (n % 2)
            {
                ans.push_back('1');
                n -= k;
            }
            else
            {
                ans.push_back('0');
            }
            k *= -1;
            n /= 2;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
// @lc code=end
