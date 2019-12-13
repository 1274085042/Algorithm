#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
2、一只青蛙一次可以跳上1级台阶，也可以跳上2级....也可以跳上n阶。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
'''
class Solution():
    def jumpFloorII(self,number):
        return pow(2,number-1)

s=Solution()
print(s.jumpFloorII(4))
