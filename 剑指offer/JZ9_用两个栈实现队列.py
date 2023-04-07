class Solution:
    """
        用两个栈实现一个队列,使用n个元素来完成n次出队列尾部插入整数(push)和n次在队列
        头部删除整数(pop)操作
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()