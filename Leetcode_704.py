"""
    给定一个n个元素有序的(升序)整型数组nums和一个目标值target
    实现函数搜索nums中的target,如果目标值存在就返回下标，否则返回-1
"""
from typing import List


class Solution:
    def search(nums:List[int], target:int)->int:
        right, left = len(nums) - 1, 0
        while left<=right:
            middle = (left + right)//2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1

if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution.search(nums, target))