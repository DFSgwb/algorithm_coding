/*
 * @lc app=leetcode.cn id=139 lang=cpp
 *
 * [139] 单词拆分
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool wordBreak(string s, vector<string> &wordDict)
    {
        set<string> St(wordDict.begin(), wordDict.end());
        int len = s.length();
        vector<bool> dp(len + 5, false);
        dp[0] = true;
        for (int i = 1; i <= len; i++)
        {
            for (int j = i; j >= 0; j--)
            {
                string lst = s.substr(j, i - j);
                if (St.find(lst) != St.end() && dp[j] == true)
                {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[len];
    }
};
// @lc code=end
