"""
    实现strStr函数:
    给你两个字符串haystack和needle,请你在haystack字符串
    中找出needle字符串出现的第一个位置,如果不存在就返回-1
"""
from torch import le


def getnext(a, needle):
        next = ['' for i in range(a)]
        j, k = 0,-1
        next[0] = k
        while(j<a-1):
            if k == -1 or needle[k] == needle[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next

class Solution:
    """
    1.KMP直接字符串匹配就可
    2.python内置函数Find()
    3.滑窗暴力破解
    """
    
    def strStr1( haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        i = j = 0
        next = getnext(a, needle)
        while(i<b and j<a):
            if j == -1 or needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j==a:
            return i-j
        else:
            return -1
    
    

    def strStr2(haystack, needle):
        """
            优雅至极,又小且快
        """
        return haystack.find(needle)
    
    
    def strStr3(haystack, needle):
        if needle == haystack:
             return 0
        Ln = len(needle)
        for i in range(len(haystack)-Ln+1):
            # 不必比较完全部字符串,如果母串剩余长度小于子串长度时还未出现结果，直接放弃即可
            if haystack[i:i+Ln] == needle:
                return i
                break
            i +=1
        return -1

if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    #osts = [[7,6,2]]
    num=Solution.strStr3(haystack,needle)
    print(num)