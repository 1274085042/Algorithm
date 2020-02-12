#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数
'''
import numpy
def solution(num):
    if num==0:
        return 0
    else:
        count=0
        while num!=0:
            mod = num % 2
            num=num//2     #//返回商的整数部分（向下取整）
            if mod==1:
                count+=1
        return count

n=int(input())
print(solution(n))



