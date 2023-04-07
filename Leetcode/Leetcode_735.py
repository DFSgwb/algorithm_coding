"""
    给定一个整数数组asyeroids,表示在同一行的行星,对于数组中的每一个元素,其绝对值表示行星大小
    正负表示行星的移动方向,正表示右,负表示左,每颗行星以相同的移动速度移动
    找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
    如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
"""
from typing import List


def asteroidCollision(asteroids:List[int])->List[int]:
    stack = []
    for ast in asteroids:
        add = True
        if ast < 0:
            while stack and stack[-1]>0 and stack[-1]<-ast:
                stack.pop()
            if stack and stack[-1]>0:
                add = False
                if stack[-1] == -ast:
                    stack.pop()
        if add:
            stack.append(ast)
    return stack

if __name__ == "__main__":
    asteroids = [5,10,-5]
    print(asteroidCollision(asteroids))