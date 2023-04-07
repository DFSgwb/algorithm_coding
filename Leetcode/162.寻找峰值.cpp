/*
 * @lc app=leetcode.cn id=162 lang=cpp
 *
 * [162] 寻找峰值
 */

// @lc code=start
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        //二分查找，查找大的一端一定会出现峰值
        int n = nums.size();
        int right=n-1, left=0;
        while(left<right){
            int mid=(left+right)/2;
            if(nums[mid]<nums[mid+1]){
                left=mid+1;
            }else{
                right=mid;
            }
        }
        return right;
    }
};
// @lc code=end

