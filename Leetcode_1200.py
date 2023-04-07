"""
    给你一个整数数组,其中每个元素都不相同,请你找出所有具有最小绝对差的元素对,并且按升序的顺序排列返回
"""
from typing import List


class Solution:
    def minimumAbsDifference(arr:List[int]) -> List[List[int]]:
        """
            排序后，相邻位置绝对值差最小
        """
        res = []
        arr = sorted(arr)
        mindff = arr[-1]-arr[0]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<mindff:
                mindff = arr[i+1]-arr[i]
                res = []
                res.append([arr[i],arr[i+1]])
            elif arr[i+1]-arr[i]==mindff:
                res.append([arr[i],arr[i+1]])
        return res
    
if __name__ == "__main__":
    arr=[3,8,-10,23,19,-4,-14,27]
    print(Solution.minimumAbsDifference(arr))
