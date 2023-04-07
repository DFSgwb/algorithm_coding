# 找到最近的相同X或Y坐标的点
from ast import List
from cmath import inf


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans, mi = -1, inf
        for i ,(a, b) in enumerate(points):
            if a==x or b==y:
                d = abs(a-x)+abs(b-y)
                if mi>d:
                    ans, mi = i, d
        return ans 