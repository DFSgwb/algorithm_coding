"""
    给定一个整数n和一个无重复黑名单整数数组blacklist。
    设计一种算法，从[0,n-1]范围内的任意整数中选取一个未加入黑名单blacklist的整数。
    任何在上述范围内且不在黑名单blacklist中的整数都应该有同等的可能性被返回
    实现Solution类:
        Solution(int n,int [] blacklist)初始化整数n和被加入黑名单blacklist的整数
        int pick()返回一个范围为[0,n-1]且不在黑名单blacklist中的随机整数
"""
from random import random
from typing import List


class Solution:
    """
        实际上可取的值只有n-m个,将m个黑名单上的值映射到n-m~n中的数字即可
    """
    def __init__(self, n:int, blacklist: List[int]):
        self.m = n-len(blacklist)
        self.st = dict()
        s = set(blacklist)
        x = self.m
        for b in blacklist:
            if b<self.m:
                while x in s:
                    x += 1
                self.st[b] = x
                x += 1

    def pick(self) ->int:
        val = random.randint(0, self.m-1)
        if val in self.st:
            return self.st[val]
        return val
