from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
        给定节点数为n的二叉树的前序遍历和中序遍历结果,请重建出该二叉树并返回它的头结点
    """
    def reConstructBinaryTree(self, pre: List[int], vin: List[int]) -> TreeNode:
        if not pre or not vin:
            return None
        root = TreeNode(pre[0])
        i = vin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:i+1], vin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], vin[i+1:])
        return root
        
