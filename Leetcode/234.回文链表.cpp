/*
 * @lc app=leetcode.cn id=234 lang=cpp
 *
 * [234] 回文链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.*/
#include <bits/stdc++.h>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    bool isPalindrome(ListNode *head)
    {
        vector<int> vt;
        while (head != nullptr)
        {
            vt.emplace_back(head->val);
            head = head->next;
        }
        for (int i = 0, j = vt.size() - 1; i < vt.size() - 1; ++i, --j)
        {
            if (vt[i] != vt[j])
                return false;
        }
        return true;
    }
};
// @lc code=end
