/*
 * @lc app=leetcode.cn id=33 lang=cpp
 *
 * [33] 搜索旋转排序数组
 */

// @lc code=start
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        if(!n){
            return -1;
        }
        if(n==1) {return nums[0]==target? 0:-1;}
        int left=0,right=n-1;
        while(left<=right){
            int mid = (left+right)/2;
            if(nums[mid]==target) return mid;
            if(nums[0]<=nums[mid]){
                if(nums[0]<=target &&target<nums[mid]){
                    right = mid-1;
                }else{
                    left=mid+1;
                }
            }else{
                if(nums[mid]<target&&target<=nums[n-1]){
                    left=mid+1;
                }else{
                    right=mid-1;
                }
            }
        }
        return -1;
    }
};
// @lc code=end

