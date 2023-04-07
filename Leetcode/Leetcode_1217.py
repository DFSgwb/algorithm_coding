"""
    有n个筹码。第i个筹码的位置是position[i]。
    我们需要把所有筹码移到同一个位置。在一步中,我们可以将第i个筹码的位置从position[i]改变为:
    position[i] + 2或position[i] - 2,此时cost = 0
    position[i] + 1或position[i] - 1,此时cost = 1
    返回将所有筹码移动到同一位置上所需要的最小代价。
"""
from typing import List


class Solution:
    # 判断数组中奇偶数的个数就可,返回其中个数少的即可
    def  minCostToMoveChips(position:List[int])->int:
        res1=0
        res2=0
        for i in range(0,len(position)):
            if position[i]%2==0:
                res1+=1
            else:
                res2+=1
        if res1>=res2:
            return res2
        else:
            return  res1

if __name__ == "__main__":
    position = [2,2,2,3,3]
    print(Solution.minCostToMoveChips(position))