
from ast import List


class Solution:
    def minOperations(self, boxes:str)->List[int]:
        """
            移动所有球到每个盒子所需的最小操作数:有n个盒子,给你一个长度为n的二进制字符串boxes,其中boxes[i]的值为'0'表示第i个盒子是空的
            而boxes[i]的值为'1'表示盒子里有一个小球。在一步操作中，你可以将 一个 小球从某个盒子移动到一个与之相邻的盒子中。
            第i个盒子和第j个盒子相邻需满足abs(i-j)==1。注意,操作执行后,某些盒子中可能会存在不止一个小球。
            返回一个长度为 n 的数组 answer ，其中 answer[i] 是将所有小球移动到第 i 个盒子所需的 最小 操作数。
        """
        res = []
        for i in range(len(boxes)):
            s = sum(abs(j - i) for j, c in enumerate(boxes) if c == '1')
            res.append(s)
        return res