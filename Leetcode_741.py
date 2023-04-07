"""
    一个N x N的网格(grid)代表了一块樱桃地，每个格子由以下三种数字的一种来表示：
    0 表示这个格子是空的，所以你可以穿过它。
    1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
    -1 表示这个格子里有荆棘，挡着你的路。
    你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：
        从位置(0,0)出发,最后到达(N-1,N-1),只能向下或向右走,并且只能穿越有效的格子(即只可以穿过值为0或者1的格子);
        当到达(N-1,N-1)后，你要继续走,直到返回到(0,0),只能向上或向左走,并且只能穿越有效的格子;
        当你经过一个格子且这个格子包含一个樱桃时,你将摘到樱桃并且这个格子会变成空的(值变为0);
        如果在(0,0)和(N-1,N-1)之间不存在一条可经过的路径,则没有任何一个樱桃能被摘到
"""
import functools
from typing import List

# 不会，抄答案
class Solution:
    def cherryPickup(grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @functools.lru_cache(None)
        def dfs(x1, y1, x2, y2):
            if not (0 <= x1 < n and 0 <= y1 < m and 0 <= x2 < n and 0 <= y2 < m): # 越界，返回负无穷
                return -float('inf')
            if grid[x1][y1] == -1 or grid[x2][y2] == -1: # 走到障碍上，返回负无穷
                return -float('inf')
            res = 0
            if x1 != x2 or y1 != y2: # 两个人走到不同位置，把两个位置的樱桃都吃掉
                res += grid[x1][y1] + grid[x2][y2]
            elif grid[x1][y1] == 1: # 两个人走到相同位置，当前位置有樱桃，则只能吃到1个
                res += 1
            if x1 == n - 1 and y1 == m - 1 and x2 == n - 1 and y2 == m - 1: # 搜索的终止条件
                return res
            res += max(dfs(x1 + 1, y1, x2 + 1, y2), dfs(x1 + 1, y1, x2, y2 + 1), dfs(x1, y1 + 1, x2 + 1, y2), dfs(x1, y1 + 1, x2, y2 + 1))
            return res
            
        return max(dfs(0, 0, 0, 0), 0) # 如果只能走到障碍上或越界那就会返回负无穷，所以要跟0取max

if __name__ == "__main__":
    grid = [[0, 1, -1],[1, 0, -1],[1, 1,  1]]
    print(Solution.cherryPickup(grid))