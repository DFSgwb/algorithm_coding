"""
    给你一个非负整数x,计算并返回x的算术平方根
    由于返回的类型是整数,结果只保留整数部分,小数部分直接舍去
"""


class Solution:
    def mySqrt(x:int)->int:
        for i in range(-1,x):
            if i*i<=x and (i+1)*(i+1)>x:
                return i 

if __name__ == "__main__":
    x = 1
    print(Solution.mySqrt(x))