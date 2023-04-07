"""
    仅使用两个栈实现先入先出队列,队列应当支持一般队列支持的所有操作
"""
class MyQueue:
    def __init__(self):
        # 声明两个负责不同功能的列表来模拟队列
        self.stack_in = []
        self.stack_out = []
    
    def push(self, x:int)->None:
        self.stack_in.append(x)
    
    def pop(self)->int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
    
    def peek(self)->int:
        res = self.pop()
        self.stack_out.append(res)
        return res
    
    def empty(self)->bool:
        return not (self.stack_in or self.stack_out)
