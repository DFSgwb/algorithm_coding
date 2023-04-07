"""
在英语中，我们有一个叫做词根(root)的概念,可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为
继承词(successor)。例如,词根an,跟随着单词other(其他)可以形成新的单词another(另一个)。
现在,给定一个由许多词根组成的词典dictionary和一个用空格分隔单词形成的句子sentence。
你需要将句子中的所有继承词用词根替换掉.如果继承词有许多可以形成它的词根,则用最短的词根替换它。
你需要输出替换之后的句子。
"""
from typing import List


class Solution:
    #将句子转化为一个一个的单词，然后直接和词根进行子串匹配即可
    
    def replaceWords(dictionary: List[str],sentence:str)->str:
        words = sentence.split()
        dictionary.sort(key=len)
        ans = " "
        for word in words:
            for root in dictionary:
                if word.startswith(root):
                    word = root
                    break
            ans = ans + word + " "
        #注意最后一个空格符号不用返回，不如数据格式对不上
        return ans[:-1]

if __name__ == "__main__":
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution.replaceWords(dictionary,sentence))
