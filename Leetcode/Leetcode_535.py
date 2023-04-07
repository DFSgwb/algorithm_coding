"""
    TinyURL是一种URL简化服务,比如:当你输入一个URL:https://leetcode.com/problems/design-tinyurl时.
    它将返回一个简化的URL http://tinyurl.com/4e9iAk 请你设计一个类来加密与解密TinyURL
    加密和解密算法如何设计和运作是没有限制的,你只需要保证一个URL可以被加密成一个TinyURL.
    并且这个TinyURL可以用解密方法恢复成原本的URL 
"""
"""
    实现 Solution 类：
    Solution()初始化TinyURL系统对象。
    String encode(String longUrl)返回longUrl对应的TinyURL。
    String decode(String shortUrl)返回shortUrl原本的URL.题目数据保证给定的shortUrl是由同一个系统对象加密的
"""
class Codec:

    def encode(longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl
        

    def decode(shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl