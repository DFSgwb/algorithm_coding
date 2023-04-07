#给你一个字符串s,你需要反转字符串中的每个单词的字符顺序,同时保留空格和单词的初始顺序
class Solution:
    def reverseWords(s:str)->str:
        # 直接按空格分割每个字符，然后内部逆序即可
        return ' '.join([i[::-1]for i in s.split(' ')])

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution.reverseWords(s))