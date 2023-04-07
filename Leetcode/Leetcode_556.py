"""
    给你一个正整数,请你找出符合条件的最小整数,其由重新排列n中存在的
    每位数字组成,并且其值大于n,如果不存在这样的整数,则返回-1
"""
"""
    解法一:单调递增栈,从后往前遍历,找到第一个小于栈内的元素,
          同时找到最小的大于该元素的值，调换两者顺序，后面元素进行重排

    解答二:直接排序遍历，首先判断一下当前数字是否为逆序，逆序则说明这个数字已经是最大的了
          如果不是逆序，然后将当前非逆序部分的第一个数字找出来，然后从右向左遍历找到第一个比这个数字大的数字与之交换即可
"""
class Solution:
    def nextGreaterElement(n:int)->int:
        INF = 1<<32-1
        n, stack = list(str(n)), []
        for i in range(len(n)-1, -1, -1):
            j = -1
            while stack and n[stack[-1]]>n[i]: #单调递增栈
                j=stack.pop() #找到栈内最小的大于当前元素的值
            if j>=0: 
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp      #调换找到的值
                n = n[:i+1]+sorted(n[i+1:]) #后面的值重排
                n = int(''.join(n))
                return n if n<=INF else -1
            stack.append(i)
        return -1
    def nextGreaterElement2( n:int)->int:
        nums = [int(x) for x in str(n)]
        if sorted(nums)[::-1] == nums:
            return -1
        m = len(nums)
        for i in range(m-2, -1,-1):
            if nums[i]<nums[i+1]:
                for j in range(m-1,i,-1):
                    if nums[j]>nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        break
                break
        res = 0
        for i in nums:
            res = 10*res+i
        return res if res<2**31 else -1

if __name__ == "__main__":
    n = 35672
    print(Solution.nextGreaterElement(n))
    print(Solution.nextGreaterElement2(n))