"""
    编写一个函数,其作用是将输入的字符串反转过来。输入字符串以字符数组s的形式给出。
    不要给另外的数组分配额外的空间,你必须原地修改输入数组、使用O(1)的额外空间解决这一问题
"""
from typing import List


class Solution:
    def reverseString(s:List[str])->None:
        n = len(s)
        # 此地不能循环全部的s长度，不然相当于交换了两次，又给还原了
        for i in range(0,n//2):
            s[i],s[n-i-1]=s[n-i-1],s[i]
        return s

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    print(Solution.reverseString(s))