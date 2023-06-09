from sympy import re


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    """
    给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
    """
    def GetNext(self, pNode):
        if not pNode:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        while pNode.next:
            if pNode.next.left == pNode:
                return pNode.next
            pNode = pNode.next
        return None
        
