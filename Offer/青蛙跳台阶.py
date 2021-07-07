#coding=utf-8

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
'''
#
# class Solution:
#     def jumFloor(self,number):
#         if number==1:
#             return 1
#         elif number==2:
#             return 2
#         else:
#             return  self.jumFloor(number-2)+self.jumFloor(number-1)


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        elif number <= 2:
            return number
        else:
            a,b = 1,2
            for i in range(2,number):
                tmp = a+b
                a=b
                b=tmp
                #a,b = b,tmp
            return b

if __name__=='__main__':
    s=Solution()
    print(s.jumpFloor(4))

# for i in range(2,2):
#     print(i)