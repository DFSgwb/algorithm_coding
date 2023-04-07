"""
    汽车从起点出发驶向目的地,该目的地位于出发位置东面target英里处.
    沿途有加油站,每个station[i]代表一个加油站,它位于出发位置东面station[i][0]英里处.
    并且有station[i][1]升汽油,假设汽车油箱的容量是无限的,其中最初有startFuel升燃料.
    它每行驶1英里就会用掉1升汽油。当汽车到达加油站时,它可能停下来加油,将所有汽油从加油站转移到汽车中.
    为了到达目的地.汽车所必需的最少加油次数是多少.如果无法到达目的地.则返回-1
"""
from typing import List
import heapq

class Solution:
    def minRefuelStops( target:int, startFuel:int, stations: List[List[int]])->int:
        """
        直接将每次经过的加油站的油全部做好标记,按站进行分堆,然后再路上行驶时没油了选择当前已经标记了的
        油站加，直接选择其中最多的就行。
        """
        if target<=startFuel:
            return 0 #不加油直接到
        heap = []
        reNumFuel = startFuel # 记录当前还剩多上油
        pos = 0 # 经过的加油站
        res = 0 # 加油次数
        while reNumFuel<target:
            for i in range(pos,len(stations)):
                if reNumFuel>=stations[i][0]:
                    heapq.heappush(heap,-stations[i][1])
                    pos+=1
            if reNumFuel<target:
                if not heap:
                    return -1
                reNumFuel-=heapq.heappop(heap)
                res+=1
        return res

if __name__ == "__main__":
    target =100
    startFuel = 10
    stations = [[10,60],[20,30],[30,30],[60,40]]
    print(Solution.minRefuelStops(target,startFuel,stations))