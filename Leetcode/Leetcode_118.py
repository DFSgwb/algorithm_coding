"""
    给定一个非负整数numRows,生成杨辉三角的前numRows行
"""
from typing import List

"""
    zip()函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元祖,
    然后返回这些有元组构成的对象
"""
class Solution:
    def gengerate(numRows:int)->List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        while len(res)<numRows:
            newRow = [a+b for a,b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)
        return res

if __name__ == "__main__":
    numRows = 5
    print(Solution.gengerate(numRows))