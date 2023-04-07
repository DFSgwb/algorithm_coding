from collections import deque

from torch import ne


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestValues(self, root):
        """
            给定一颗二叉树的根节点root,请找出该二叉树中每一层的最大值
        """
        """
            :type root: TreeNode
            :rtype: List[int]
        """
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            next_layer = []
            cur_layer_max = float("-inf")
            while q:
                node = q.popleft()
                cur_layer_max = max(cur_layer_max, node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            ans.append(cur_layer_max)
            q = deque(next_layer)
        return ans