"""
    给定字符串形式的两个非负整数num1和num2,计算它们的和并同样以字符串形式返回
"""
class Solution:
    def addStrings( num1:str, num2:str)->str:
        i=len(num1)-1
        j=len(num2)-1
        res=""
        temp = 0
        while i>=0 or j>=0:
            n1 =  int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            use = n1 + n2 + temp
            temp = use//10
            res = str(use%10)+res
            i-=1
            j-=1
        return "1" +res if temp else res

if __name__ == "__main__":
    num1 = "11"
    num2 = "123"
    print(Solution.addStrings(num1, num2))