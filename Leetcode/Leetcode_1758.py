"""
    给你一个仅由字符"0"和"1"组成的字符串s,一步操作中将任一"0"和"1"相互变换,寻找最小将给定字符变化为交替字符串的操作数
"""
class Solution:
    def minOperation(s:str) -> int:
        """
            本质上就是寻找给定字符010101...或者10101010...之间的最小差异值
        """
        n = len(s)
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if s[i] != str(i%2): 
                cnt1 += 1
            else:
                cnt2 += 1
        
        return min(cnt1, cnt2);

if __name__ == '__main__':
    digit = "1111"
    num=Solution.minOperation(digit)
    print(num)