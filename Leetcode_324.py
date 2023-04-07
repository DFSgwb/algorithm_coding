"""
    给你一个整数数组nums,将它重新排列成nums[0]<nums[1]>nums[2]<numn[3]...的顺序
"""
from typing import List

from numpy import append

"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[1::2],nums[0::2] = nums[:mid], nums[mid:]
"""
class Solution:
    def wiggleSort(nums:List) -> None:
        nums.sort(reverse=False)
        n=len(nums)
        res = []
        mid = n // 2
        for i in range(0,mid):
            res.append(nums[i])
            res.append(nums[mid+i])
        return res

if __name__ == '__main__':
    nums = [1,5,1,1,6,4]
    print(sorted(nums))
    num=Solution.wiggleSort(nums)
    print(num)
