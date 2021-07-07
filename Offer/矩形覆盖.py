#coding=utf-8

class Solution():
    def rectCover(self,number):
        if number==1:
            return 1
        elif number==2:
            return 2
        else:
            a,b=1,2
            for i in range(2,number):
                tmp=a+b
                a=b
                b=tmp
            return b


s=Solution()
print(s.rectCover(4))


