#coding=utf-8

'''
题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
'''

def str_sort(n):
    str_list=[]
    for i in range(n):
        str=input()
        str_list.append(str)
    str_list.sort()
    for s in str_list:
        print(s)
n=int(input())
str_sort(n)