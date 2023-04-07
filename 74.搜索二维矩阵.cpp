/*
 * @lc app=leetcode.cn id=74 lang=cpp
 *
 * [74] 搜索二维矩阵
 */

// @lc code=start
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // 拉平二维数组，直接二分查找即可
        int n=matrix.size();
        int m=matrix[0].size();
        int right = n*m-1, left=0;
        while(left<=right){
            int mid=(right-left)/2+left;
            int res=matrix[mid/m][mid%m];
            if(res<target){
                left=mid+1;
            }else if(res>target){
                right = mid-1;
            }else{
                return true;
            }
        }
        return false;
    }
};
// @lc code=end

