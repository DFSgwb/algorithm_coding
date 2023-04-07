/*
 * @lc app=leetcode.cn id=347 lang=cpp
 *
 * [347] 前 K 个高频元素
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> mp;
        vector<int> res;
        priority_queue<pair<int, int>> pq;
        for (int i = 0; i < nums.size(); i++)
            mp[nums[i]]++;
        for (auto p : mp)
        {
            pq.push(pair<int, int>(-p.second, p.first));
            if (pq.size() > k)
                pq.pop();
        }
        while (k--)
        {
            res.push_back(pq.top().second);
            pq.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
// @lc code=end
