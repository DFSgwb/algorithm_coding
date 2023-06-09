# Definition for a binary tree node.
"""
给你一个二叉树的根结点 root,请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

"""


from typing import Counter, List


class TreeNode:
    def __init__(self, val=0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cnt[left + right + node.val] += 1
            return left + right + node.val
        dfs(root)
        maxCnt = max(cnt.values())
        return [s for s, c in cnt.items() if c == maxCnt]
