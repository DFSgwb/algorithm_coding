"""
    我的日程安排.实现一个MyCalendar类来存放你的日程安排,如果要添加的日程安排不会造成重复预订,则可以存储这个新的日程安排
    当两个日程安排出现实现上的交叉时,就会产生重复预订。
    日程可以用一对整数表示
"""

from bisect import bisect, bisect_right



class MyCalendar:
    def __init__(self):
        self.lst = []
        """
            bisect是python的内置模块,用于有序序列的插入和查找
            bisect(array,item)查找
            insort(array,item)插入
        """
    def book(self, start:int, end:int)->bool:
        if not self.lst:
            #使用bisect.insort比bisect先查找该插入的位置再用insert插入更快
            bisect.insort(self.lst,start)
            bisect.insort(self.lst,end)
            return True
        idx=bisect_right(self.lst,start)
        if idx==len(self.lst) or idx%2==0 and self.lst[idx]>=end:
            bisect.insort(self.lst,start)
            bisect.insort(self.lst,end)
            return True
        return False

if __name__ == "__main__":
    list = [[], [10, 20], [15, 25], [20, 30]]
    print(MyCalendar.book(list))

    