/*
 * @lc app=leetcode.cn id=38 lang=cpp
 *
 * [38] 外观数列
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    string countAndSay(int n)
    {
        if (n == 1)
            return "1";
        string last = countAndSay(n - 1);
        string res;
        for (int i = 0; i < last.size(); i++)
        {
            int j = i;
            while (j + 1 < last.size() && last[j + 1] == last[j])
            {
                j++;
            }
            res += to_string(j - i + 1) + last[i];
            i = j;
        }
        return res;
    }
};
// @lc code=end
