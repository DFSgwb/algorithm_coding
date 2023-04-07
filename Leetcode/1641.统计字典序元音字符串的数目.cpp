/*
 * @lc app=leetcode.cn id=1641 lang=cpp
 *
 * [1641] 统计字典序元音字符串的数目
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int countVowelStrings(int n)
    {
        // 组合数学
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24;
    }
};
// @lc code=end
