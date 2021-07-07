#coding=utf-8

'''
编写一个函数，计算字符串中含有的不同字符的个数。
字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。
'''

def count(str):
    k=[]
    str_list=list(str)
    str_set=set(str_list)
    #print(str_set)
    #print(type(str_set))
    print(len(str_set))
s=input()
count(s)
