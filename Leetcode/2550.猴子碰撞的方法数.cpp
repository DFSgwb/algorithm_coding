/*
 * @lc app=leetcode.cn id=2550 lang=cpp
 *
 * [2550] 猴子碰撞的方法数
 */

// @lc code=start
class Solution
{
public:
    int monkeyMove(int n)
    {
        unsigned long ans = 1;
        for (; n > 32; n -= 32)
        {
            ans <<= 32;
            ans %= 1000000007;
        }
        while (n--)
        {
            ans <<= 1;
            ans %= 1000000007;
        }
        return (ans + 1000000005) % 1000000007;
    }
};
// @lc code=end
