#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
输入一个整数，输出该数二进制表示中1的个数，其中负数用补码表示

思路：
100转换为二进制:
100/2=50....(余数为0);
50/2=25.....(余数为0);
25/2=12.....(余数为1);
12/2=6......(余数为0);
6/2=3.......(余数为0);
3/2=1.......(余数为1);
1/2=0.......(余数为1);
所以100的二进制表示形式为1100100;
'''

# class Solution():
#     def zhengshu(self,n,total,one_num):
#         while n != 0:
#             total += 1
#             y = n % 2
#             n = n // 2
#             if y == 1:
#                 one_num += 1
#         return one_num,total
#
#     def Numberof1(self,n):
#         one_num=0
#         total=1
#         if n<0:
#             if n==-2147483648:
#                 return 1
#             n=-n
#             one_num, total = self.zhengshu( n, total, one_num )
#             one_num=total+1-one_num
#
#         else:
#             one_num,total=self.zhengshu(n,total,one_num)
#
#         return one_num
#
# s=Solution()
# print(s.Numberof1(-2147483648))

class Solution():
    def Numberof1(self,n):
        count=0
        for i in  range(32):
            if(n>>i&1):
                count+=1
        return count

s=Solution()
print(s.Numberof1(3))