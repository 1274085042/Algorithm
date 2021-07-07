#coding=utf-8

'''
题目描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。
'''

#int() 函数用于将一个字符串或数字转换为整型。
while True:
    try:
        str=input()
        res=int(str,16)
        print(res)
    except:
        break