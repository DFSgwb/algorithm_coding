"""
    给定一个非负索引rowIndex,返回杨辉三角的第rowIndex行
"""
from typing import List


class Solution:
    def getRow(rowIndex: int) -> List[int]:
        res = [1]*(rowIndex+1)
        for i in range(1,len(res) - 1):
            res[i] = res[i-1]*(rowIndex-i+1)//i
        return res

if __name__ == "__main__":
    rowIndex = 5
    print(Solution.getRow(rowIndex))
        