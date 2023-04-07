# 设计一个使用单词列表进行初始化数据结构,单词列表中的单词互不相同,如果给出一个单词
# 请判定能否只将这个单词中一个字母换成另一个字母使得所形成的单词存在于你构建的字典中

"""
    实现 MagicDictionary 类：
    MagicDictionary() 初始化对象
    void buildDict(String[]dictionary)使用字符串数组dictionary设定该数据结构,dictionary中的字符串互不相同
    bool search(String searchWord)给定一个字符串searchWord,判定能否只将字符串中一个字母换成另一个字母,
    使得所形成的新字符串能够与字典中的任一字符串匹配.如果可以,返回true否则,返回false 
"""
from collections import defaultdict
from typing import List



class MagicDictionary:
    def __init__(self) -> None:
        self.mp = defaultdict(list)
    def buildDict(self, dictionary:List[str])->None:
        for d in dictionary:
            self.mp[len(d)].append(d)

    def search(self, searchWord:str)->bool:
        for d in self.mp[len(searchWord)]:
            if sum(c0 != c1 for c0, c1 in zip(searchWord, d)) == 1:
                return True
        return False
