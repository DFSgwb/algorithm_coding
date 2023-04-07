/*
 * @lc app=leetcode.cn id=153 lang=cpp
 *
 * [153] 寻找旋转排序数组中的最小值
 */

// @lc code=start
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int findMin(vector<int>& nums) {
        //相当于寻找当前nums最小值的下标，注意：当下标为0时，旋转次数为一轮
        int left = 0, right=nums.size()-1;
        while(left<right){
            int mid = (right+left)/2;
            if(nums[mid]<nums[right]){
                right=mid;
            }else{
                left=mid+1;
            }
        }
        return nums[left];
    }
};
// @lc code=end

