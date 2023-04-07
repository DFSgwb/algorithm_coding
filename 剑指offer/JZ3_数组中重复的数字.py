from typing import List


class Solution:
    """
    在长度为n的数组里的所有数字都在0到n-1的范围内。
    数组中某些数字是重复的，但不知道有几个数字是重复的。
    也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
    """
    def duplicate(self, numbers:List[int])->int:
        if not numbers:
            return -1
        numbers.sort()
        for i in range(1,len(numbers)):
            if numbers[i]==numbers[i-1]:
                return numbers[i]
        return -1
        