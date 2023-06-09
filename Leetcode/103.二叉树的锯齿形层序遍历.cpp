/*
 * @lc app=leetcode.cn id=103 lang=cpp
 *
 * [103] 二叉树的锯齿形层序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 */
#include <bits/stdc++.h>
using namespace std;
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode *root)
    {
        // 定义答案数组
        vector<vector<int>> ans;
        if (!root)
        {
            return ans;
        }
        queue<TreeNode *> nodeQueue;
        nodeQueue.push(root);
        bool isOrderLeft = true;
        while (!nodeQueue.empty())
        {
            deque<int> levelList;
            int size = nodeQueue.size();
            for (int i = 0; i < size; i++)
            {
                auto node = nodeQueue.front();
                nodeQueue.pop();
                if (isOrderLeft)
                {
                    levelList.push_back(node->val);
                }
                else
                {
                    levelList.push_front(node->val);
                }
                if (node->left)
                {
                    nodeQueue.push(node->left);
                }
                if (node->right)
                {
                    nodeQueue.push(node->right);
                }
            }
            ans.emplace_back(vector<int>{levelList.begin(), levelList.end()});
            isOrderLeft = !isOrderLeft;
        }
        return ans;
    }
};
// @lc code=end
