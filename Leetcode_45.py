from typing import List


def jump(nums: List[int]) -> int:
        start = step = 0
        end = 1
        n = len(nums)
        while end < n:
            max_num = 0
            for i in range(start,end):
                max_num = max(max_num, i+nums[i])
            
            start,end,step = end,max_num + 1,step+1
            # print(start,end,max_num,step)

        return step

if __name__ == "__main__":
        nums = list(map(int, input().split(' ')))
        print(jump(nums))