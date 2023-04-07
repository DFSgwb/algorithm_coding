/*
 * @lc app=leetcode.cn id=496 lang=cpp
 *
 * [496] 下一个更大元素 I
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        stack<int> st;
        vector<int> result(nums1.size(), -1);
        if (nums1.size() == 0)
            return result;
        unordered_map<int, int> mp;
        for (int i = 0; i < nums1.size(); i++)
        {
            mp[nums1[i]] = i;
        }
        st.push(0);
        for (int i = 1; i < nums2.size(); i++)
        {
            while (!st.empty() && nums2[i] > nums2[st.top()])
            {
                if (mp.count(nums2[st.top()]))
                {
                    int index = mp[nums2[st.top()]];
                    result[index] = nums2[i];
                }
                st.pop();
            }
            st.push(i);
        }
        return result;
    }
};
// @lc code=end
