"""
    设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。
    实现WordFilter类:
    WordFilter(string[] words) 使用词典中的单词 words 初始化对象。
    f(string pref, string suff) 返回词典中具有前缀 prefix和后缀suff的单词的下标。
    如果存在不止一个满足要求的下标，返回其中 最大的下标 。如果不存在这样的单词，返回 -1 。
"""
from typing import List


class WorldFilter:
    def __init__(self, words:List[str]):
        self.map = {}
        for i ,word in enumerate(words):
            for j in range(1,len(word)+1):
                for k in range(1,len(word)+1):
                    self.map[(word[:j],word[-k:])]=i


    def f(self, pref:str,suff:str)->int:
        return self.map.get((pref,suff),-1)