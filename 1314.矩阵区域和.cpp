/*
 * @lc app=leetcode.cn id=1314 lang=cpp
 *
 * [1314] 矩阵区域和
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>> &mat, int k)
    {
        // 首先获取矩阵的长宽m，n
        int m = mat.size();
        int n = mat[0].size();
        // 确定求取矩阵的边界,然后使用对应的框在矩阵内部框区域即可
        vector<vector<int>> P(m + 1, vector<int>(n + 1));
        for (int i = 1; i <= m; ++i)
        {
            for (int j = 1; j <= n; ++j)
            {
                // 其中p[i][j]表示[i,j]->[0,0]所框起来的矩阵中的元素和
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1];
            }
        }
        vector<vector<int>> ans(m, vector<int>(n));
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                ans[i][j] = get(P, m, n, i + k + 1, j + k + 1) - get(P, m, n, i - k, j + k + 1) - get(P, m, n, i + k + 1, j - k) + get(P, m, n, i - k, j - k);
            }
        }
        return ans;
    }
    int get(vector<vector<int>> &pre, int m, int n, int x, int y)
    {
        x = max(min(x, m), 0);
        y = max(min(y, n), 0);
        return pre[x][y];
    }
};
// @lc code=end
