"""
    给定一个由整数组成的非空数组所表示的非负整数,在该数的基础上加一。
    最高位数字存放在数组的首位,数组中每个元素只存储单个数字。
    你可以假设除了整数0之外,这个整数不会以零开头。
"""
from typing import List


class Solution:
    def plusOne(digits:List[int]) -> List[int]:
        return list(map(int,str(int(''.join(map(str,digits)))+1)))


if __name__ == "__main__":
    digits = [1,2,3]
    print(Solution.plusOne(digits))