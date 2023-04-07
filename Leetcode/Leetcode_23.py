# 给你一个链表数组,每个链表都已经按升序排列,请你将所有链表合并到一个升序链表中,返回合并后的链表
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeList(lists:List[Optional[ListNode]]) -> Optional[ListNode]:
        # 直接将所有链表中的值全部丢到一个数组中，然后对数组直接排序即可
        nums = []
        for l in lists:
            j=l
            while j:
                nums.append(j.val)
                j=j.next
        nums.sort()
        res = ListNode(0)
        head = res
        for i in range(len(nums)):
            head.next = ListNode(nums[i])
            head = head.next
        return res.next

if __name__ == "__main__":
    lists = ListNode([[1,4,5],[1,3,4],[2,6]])
    print(Solution.mergeList(lists))