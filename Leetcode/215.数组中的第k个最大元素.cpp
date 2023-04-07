/*
 * @lc app=leetcode.cn id=215 lang=cpp
 *
 * [215] 数组中的第K个最大元素
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;
/* class Solution
{
private:
    int priorityThan(int i, int j) { return i < j; }
    void bulidheap(vector<int> &nums, int i)
    {
        while (i > 0 && priorityThan(nums[i], nums[(i - 1) / 2]))
        {
            swap(nums[i], nums[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }
    void buildheap2(vector<int> &nums, int i, int j)
    {
        while (2 * i + 1 <= j)
        {
            int m = 2 * i + 1;
            if (m + 1 <= j && priorityThan(nums[m + 1], nums[m]))
            {
                m++;
            }
            if (priorityThan(nums[i], nums[m]))
            {
                break;
            }
            swap(nums[i], nums[m]);
        }
    }

public:
    int findKthLargest(vector<int> &nums, int k)
    {
        // 前n个数建堆
        for (int i = 0; i < k; i++)
        {
            bulidheap(nums, i);
        }
        for (int i = k; i < nums.size(); i++)
        {
            if (nums[i] > nums[0])
            {
                swap(nums[0], nums[i]);
                buildheap2(nums, 0, k - 1);
            }
        }
        return nums[0];
    }
};*/

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        priority_queue<int, vector<int>, greater<>> q;
        for (const auto &num : nums)
        {
            if (q.size() < k)
            {
                q.push(num);
            }
            else if (q.top() < num)
            {
                q.pop();
                q.push(num);
            }
        }
        return q.top();
    }
};
// @lc code=end
