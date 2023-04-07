/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start

/*Definition for singly-linked list.
 **/
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
    ListNode *reverseKGroup(ListNode *head, int k)
    {
        int n = 0;
        for (ListNode *cur = head; cur; cur = cur->next)
            ++n;
        ListNode *res = new ListNode(0, head), *p = res;
        ListNode *pre = nullptr, *cur = head;
        for (; n >= k; n -= k)
        {
            for (int i = 0; i < k; ++i)
            {
                ListNode *next = cur->next;
                cur->next = pre;
                pre = cur;
                cur = next;
            }
            ListNode *next = p->next;
            p->next->next = cur;
            p->next = pre;
            p = next;
        }
        return res->next;
    }
};
// @lc code=end
