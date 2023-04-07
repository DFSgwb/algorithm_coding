"""
    给定一颗二叉搜索树,找到该树中两个指定节点的最近公共祖先
"""

from sympy import root


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode')->'TreeNode':
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

if __name__ == "__main":
    root = [6,2,8,0,4,7,9,None,None,3,5]
    p=2
    q=8
    print(Solution.lowestCommonAncestor(root,p,q))