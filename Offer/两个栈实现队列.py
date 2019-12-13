#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
用两个栈来实现一个队列操作，完成队列中的push和pop操作
'''

class Solution():
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def Push(self,x):
        self.stack_in.append(x)

    def Pop(self):
        if self.stack_out==[]:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

s=Solution()
s.Push(1)
s.Push(2)
print(s.stack_in)
print(s.Pop())
print(s.stack_in)
print(s.Pop())
print(s.stack_out)

