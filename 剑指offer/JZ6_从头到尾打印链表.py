from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    """
        输入一个链表,按链表值从尾到头的顺序返回每个节点的值。
    """
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        if not ListNode:
            return []
        result = []
        while listNode:
            result.append(listNode.val)
            listNode = listNode.next
        return result[::-1]