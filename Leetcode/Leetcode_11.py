#给定一个长度为n的整数数组height，其中有n调垂线，第i条线的两个端点是
#（i,0）和（i,height[i]）找出其中的两条线，使得它们与x轴共同构成的容器
#可以容纳最多的水
from typing import List


class Solution:
    def maxArea(height:List[int])->int:
        i, j=0, len(height)-1
        maxarea = 0
        while i<j:
            h, w = min(height[i],height[j]),j-i
            maxarea = max(maxarea, h*w)
            curr = min(height[i],height[j])
            if height[i]<height[j]:
                while height[i]<=curr and i < j:
                    i += 1
            else:
                while height[j] <= curr and i<j:
                    j -= 1
        return maxarea

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution.maxArea(height))