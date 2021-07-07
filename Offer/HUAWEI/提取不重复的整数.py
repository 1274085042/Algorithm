#coding=utf-8

'''
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
'''
num=list(input())
num=num[::-1]
res=[]
for i in num:
    if i not in res:
        res.append(i)
res_num="".join(res)
print(int(res_num))