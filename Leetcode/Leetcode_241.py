"""
    给你一个由数字和运算符组成的字符串expression,按不同优先级组合数字和运算符,计算并返回所有可能组合的结果,你可以按任意顺序返回答案
"""
from functools import lru_cache
from itertools import product
import operator
import re
from typing import List


OP_MAP = {"+": operator.add, "-": operator.sub, "*": operator.mul}
class Solution:
    def diffWaysToCompute(expression: str) -> List[int]:
        @lru_cache(None)
        def dfs(left: int, right: int) -> List[int]:
            if left == right:
                return [int(sp[left])]
            return [OP_MAP[sp[i]](left_set, right_set) for i in range(left+1,right,2) for left_set,right_set in product(dfs(left,i-1),dfs(i+1,right))]
            
        sp = re.split(r"(\D)", expression)
        return list(dfs(0, len(sp) - 1))
    
if __name__ == "__main__":
    expression = "2-1-1"
    print(Solution.diffWaysToCompute(expression))
