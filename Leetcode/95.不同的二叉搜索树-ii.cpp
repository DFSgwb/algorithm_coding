/*
 * @lc app=leetcode.cn id=95 lang=cpp
 *
 * [95] 不同的二叉搜索树 II
 */

// @lc code=start


#include<bits/stdc++.h>
using namespace std;
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };
/* 
 * Definition for a binary tree node.
*/
class Solution {
public:
    vector<TreeNode*> dfs(int l,int r){
        if(l>r)
            return {nullptr};
        vector<TreeNode*> res;
        for(int k=l;k<=r;k++){
            auto left=dfs(l,k-1), right=dfs(k+1, r);
            for(auto& l:left){
                for(auto& r:right){
                    auto root = new TreeNode(k);
                    root->left=l;
                    root->right=r;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
    vector<TreeNode*> generateTrees(int n) {
        return dfs(1, n);
    }
};
// @lc code=end

