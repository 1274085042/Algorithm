#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）
'''

def get_input(n):
    items={}
    for i in range(n):
        item=input()
        item=item.split()
        k=int(item[0])
        v=int(item[1])
        if k not in items.keys():
               items[k]=v
        else:
            items[k]+=v
    items=sorted(items.items(),key=lambda item:item[0])  #items.items()将items转化为可迭代对象
    for k,v in items:
        print(k,v)
    #print(items.items())
    #print(items.keys())
n=int(input())
get_input(n)