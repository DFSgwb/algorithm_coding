"""
    地上有一个 rows 行和 cols 列的方格。坐标从 [0,0] 到 [rows-1,cols-1] 。
    一个机器人从坐标 [0,0] 的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于 
    threshold 的格子。 例如，当 threshold 为 18 时，机器人能够进入方格[35,37],
    因为 3+5+3+7 = 18。但是,它不能进入方格 [35,38] ，因为 3+5+3+8 = 19 。请问该机器人能够达到多少个格子？
"""
class Solution:
    def movingCount(self , threshold: int, rows: int, cols: int) -> int: