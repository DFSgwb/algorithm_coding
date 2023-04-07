import queue
from tkinter.messagebox import NO
from typing import Deque, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, return the leftmost value in the last row of the tree.
    """
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue, ans = Deque([root]), None
        while queue:
            ans = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans