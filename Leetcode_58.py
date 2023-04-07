"""
    给你一个字符串s,由若干单词组成,单词前后用一些空格字符隔开,
    返回字符串中最后一个单词的长度
"""
class Solution:
    def LengthOfLastWord(s:str)->int:
        return len(s.split( )[-1])

if __name__ == "__main__":
    s = "Hello World"
    print(Solution.LengthOfLastWord(s))
