/*
 * @lc app=leetcode.cn id=973 lang=cpp
 *
 * [973] 最接近原点的 K 个点
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<vector<int>> kClosest(vector<vector<int>> &points, int k)
    {
        // 使用一个vector来存每一个距离的平方
        vector<vector<int>> ans;
        priority_queue<pair<int, int>> q;
        // 使用一个二维数组来存储结果
        vector<vector<int>> res;
        int temp;
        for (int i = 0; i < k; ++i)
        {
            int x = points[i][0];
            int y = points[i][1];
            temp = x * x + y * y;
            q.emplace(temp, i);
        }
        // 使用优先队列将距离为前K个挑选出来
        int n = points.size();
        for (int i = k; i < n; ++i)
        {
            int x = points[i][0];
            int y = points[i][1];
            int dist = x * x + y * y;
            if (dist < q.top().first)
            {
                q.pop();
                q.emplace(dist, i);
            }
        }
        while (!q.empty())
        {
            ans.push_back(points[q.top().second]);
            q.pop();
        }
        return ans;
    }
};
// @lc code=end
