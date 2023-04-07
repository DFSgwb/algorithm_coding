"""
    给你一个mxn的矩阵,最开始的时候,每个单元格中的值都是0。
    另有一个二维索引数组indices,indices[i]=[ri,ci]指向矩阵中的某个位置,其中ri和ci分别表示指定的行和列(从0开始编号)。
    对indices[i]所指向的每个位置,应同时执行下述增量操作：
    ri行上的所有单元格,加1。
    ci列上的所有单元格,加1。
    给你m、n和indices.请你在执行完所有indices指定的增量操作后,返回矩阵中奇数值单元格的数目
"""
from typing import List


def oddCells(m:int,n:int,indices:List[List[int]])->int:
    c1, c2 = 0, 0
    for i, j in indices:
        c1 ^= (1 << i)
        c2 ^= (1 << j)
    a, b = 0, 0
    for i in range(m):
        a += (c1 >> i) & 1
    for i in range(n):
        b += (c2 >> i) & 1
    return a * (n - b) + (m - a) * b

if __name__ == "__main__":
    m = 2
    n = 3
    indices = [[0,1],[1,1]]
    print(oddCells(m,n,indices))