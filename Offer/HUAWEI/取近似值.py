#coding=utf-8

'''
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值
'''
import math

def quzheng(num):
    num=float(num)
    xiaoshu=math.modf(num)[0]
    zhengshu=int(math.modf(num)[1])
    if xiaoshu>=0.5:
        print(zhengshu+1)
    else:
        print(zhengshu)

num=input()
quzheng(num)