from typing import List
from collections import Counter

class Solution:
    """
    给定一个字符串s和一些长度相同的单词words,找出s中恰好可以由words中所有单词串联
    形成子串的起始位置,注意子串要与words中的单词完全匹配,中间不能有其他字符,但不需要考虑
    words中单词串联的顺序
    """
    """
    记words的长度为 m,words 中每个单词的长度为 n,s的长度为ls。首先需要将 ss 划分为单词组，每个单词的大小均为nn首尾除外。
    这样的划分方法有 nn 种，即先删去前i,i=0∼n−1个字母后，将剩下的字母进行划分，如果末尾有不到 nn 个字母也删去。
    对这 nn 种划分得到的单词数组分别使用滑动窗口对words 进行类似于「字母异位词」的搜寻。
    划分成单词组后，一个窗口包含 s 中前mm个单词，用一个哈希表 differ 表示窗口中单词频次和words中单词频次之差。
    初始化differ时，出现在窗口中的单词，每出现一次，相应的值增加 11，出现在words 中的单词，
    每出现一次，相应的值减少1。然后将窗口右移，右侧会加入一个单词，左侧会移出一个单词，并对differ 做相应的更新。
    窗口移动时，若出现differ 中值不为 00 的键的数量为 00，则表示这个窗口中的单词频次和words 中单词频次相同，
    窗口的左端点是一个待求的起始位置。划分的方法有 nn 种，做 nn 次滑动窗口后，即可找到所有的起始位置。
    """
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        one_words = len(words[0])
        word_nums = len(words)
        n = len(s)
        if n < one_words:
            return []
        words = Counter(words)
        res = []
        for i in range(0, one_words):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_words <= n:
                w = s[right:right+one_words]
                right += one_words
                if w not in words:
                    left = right 
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_words]
                        left += one_words
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_nums:
                        res.append(left)
        return res
