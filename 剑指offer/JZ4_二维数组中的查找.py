from typing import List


class Solution:
    """
    在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
    """
    def Find(self, target:int, array: List[List[int]]) -> bool:
        if not array:
            return False
        row = len(array)
        col = len(array[0])
        i = row - 1
        j = 0
        while i >= 0 and j < col:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                i -= 1
            else:
                j += 1
        return False