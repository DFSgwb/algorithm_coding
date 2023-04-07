from typing import List

from sympy import false, true


class Solution:
    """
    请设计一个函数,用来判断在一个n乘m的矩阵中是否存在一条包含某长度为len的字符串所有字符的路径。
    路径可以从矩阵中的任意一个格子开始,每一步可以在矩阵中向左，向右，向上，
    向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
    """
    def hasPath(self , matrix: List[List[str]], word: str) -> bool:
        visited = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.DFS(i, j, matrix, visited, word):
                    return True
        return False
     
    def DFS(self, x, y, matrix, visited, word):
        if not word:
            return True
        if not visited[x][y]:
            if matrix[x][y] == word[0]:
                if len(word)==1:
                    return True
                visited[x][y]=1
                if y+1 <= len(matrix[0])-1 and self.DFS(x,y+1, matrix, visited, word[1:]):
                    return True
                if x+1 <= len(matrix)-1 and self.DFS(x+1,y, matrix, visited, word[1:]):
                    return True
                if x-1 >= 0 and self.DFS(x-1,y, matrix, visited, word[1:]):
                    return True
                if y-1 >= 0 and self.DFS(x,y-1, matrix, visited, word[1:]):
                    return True
                visited[x][y]=0
        return False