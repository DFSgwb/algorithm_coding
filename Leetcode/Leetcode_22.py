"""
    数字n代表生成括号的对数,请你设计一个函数,用于能够生成所有可能的并且有效的括号组合
"""
from turtle import right

from torch import le


class Solution:
    """
    dfs+回溯：
    左括号相当于向左建立子树,右括号相当于向右建立子树
    将括号转化为树节点上的值,配合当向左建立分支数目和向右建立分支数目相等时,
    下一步只能向左边建立分支进行剪纸
    """
    def generateParenthesis(n):
        """
            :type n :int
            :rtype: List[str]
        """
        res = []
        cur_str = ''
        def dfs(cur_str, left, right):
            """
                left,right:分别表示当前可用左右括号的数目
            """
            if left == 0 and right==0:
                res.append(cur_str)
                return 
            if right<left:
                return
            if left >0:
                dfs(cur_str+'(',left-1,right)
            if right>0:
                dfs(cur_str+')',left, right-1)

        dfs(cur_str, n, n)
        return res

if __name__ == '__main__':
    n = 3
    num=Solution.generateParenthesis(n)
    print(num)