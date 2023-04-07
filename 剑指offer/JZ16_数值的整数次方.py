class Solution:
    """
        实现函数double Power(double base, int exponent),求base的exponent次方。
    """
    def Power(self, base:float, exponent: int)->float:
        if base == 0.0:
            return 0.0
        if exponent == 0:
            return 1.0
        if exponent < 0:
            base = 1/base
            exponent = -exponent
        ans = 1
        tmp = base
        while(exponent):
            if exponent&1:
                ans *= tmp
            tmp *= tmp
            exponent = exponent >> 1
        return ans
if __name__ == '__main__':
    num=Solution.Power(2.00000, 3)
    print(num)