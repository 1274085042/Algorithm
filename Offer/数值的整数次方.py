#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

class Solution():
    def Power(self,base,expoent):
        flag=0
        if base==0:
            return 0
        if expoent==0:
            return 1
        elif expoent<0:
            flag=1

        result=base
        expoent=abs(expoent)
        while(expoent!=1):
            result=result*base
            expoent-=1
        if flag==0:
            return result
        else:
            return 1/result
s=Solution()
print(s.Power(0.1,3))
