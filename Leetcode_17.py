"""
    给定一个仅包含数字2-9的字符串,返回所有它能表示的字母组合,答案可以按任意顺序返回
    数字与字母的映射方式和九键电话上相同
"""
import collections
from typing import  List

from pip import main


class Solution:
    """
        建立数字和字符之间映射的哈希表,然后配合队列使用深度优先遍历进行字符组合
    """
    def letterCombinations(digits: str) -> List[str]:
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
               '9': 'wxyz'}

        if len(digits)==0:
            return []
        q = collections.deque()
        q.extend(dic[digits[0]]) #首先将数字字符串中的第一个数字压入到队列中
        digits = digits[1:] #将这个数字从字符串中移除，为了方便构建结束条件
        while digits: #当数字字符串不为空时，此时表示还需要有新的字母组合
            for i in range(len(q)): #因为每个数字对应的字母均要用来进行字母组合，所以这边需要知道每一层的字母个数
                tmp = q.popleft() #首先将第一个元素弹出
                for j in range(len(dic[digits[0]])): #将第一个元素弹出，此时需要与第二个数字对应
#的字母进行组合，每个字母均需要，所以这边要按照长度进行遍历
                    tmp1 = tmp + dic[digits[0]][j] #将弹出的元素和新的字母进行组合
                    q.append(tmp1) #组合后放入队列中
            digits = digits[1:] #将这个已经组合完成的数字移除
        res = [] #因为刚刚元素均存在了队列中，此时需要返回一个数组，所以需要重新初始化一个数组
        for p in range(len(q)): #将队列中的每一个元素弹出，并放入到结果数组中
            tmp_pop = q.popleft() #将队列中元素弹出
            res.append(tmp_pop) #放入结果数组中
        return res 

if __name__ == '__main__':
    digit = "23"
    num=Solution.letterCombinations(digit)
    print(num)

