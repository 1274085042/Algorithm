#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.

from threading import  Thread
import time

class Solution():
    def __init__(self,list):
        self.list=list
        self.result=[]

    def Sleep(self,x):
        time.sleep(x*0.01)
        self.result.append(x)


    def Sort(self):
        r=[]
        threads=[]
        for i in self.list:
            t=Thread(target=self.Sleep,args=(i,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

s=Solution([1,6,5,7,9,4])
s.Sort()

print(s.result)
