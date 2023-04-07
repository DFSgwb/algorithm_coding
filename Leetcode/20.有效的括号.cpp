/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool isValid(string s)
    {
        if (s.size() % 2 != 0)
            return false;
        stack<char> st;
        for (char ch : s)
        {
            if (ch == '(')
            {
                st.push(')');
            }
            else if (ch == '[')
            {
                st.push(']');
            }
            else if (ch == '{')
            {
                st.push('}');
            }
            else if (!st.empty() && ch == st.top())
            {
                st.pop();
            }
            else if (st.empty() || ch != st.top())
            {
                return false;
            }
        }
        return st.empty();
    }
};
// @lc code=end
