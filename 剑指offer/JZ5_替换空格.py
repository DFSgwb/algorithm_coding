class Solution:
    """
    将一个字符串s中的每个空格替换成"%20"
    """
    def replaceSpace(self, s:str)->str:
        return s.replace(" ", "%20")
