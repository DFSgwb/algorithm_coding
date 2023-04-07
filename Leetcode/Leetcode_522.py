"""
    给定字符串列表strs,返回其中最长的特殊序列,如果最长特殊序列不存在,返回-1
    特殊序列定义如下:该序列某字符串独有的子序列(即不能是其他字符串的子序列)
"""
from typing import List


class Solution:
    def findLUSlength(self, strs:List[str]) -> int:
        