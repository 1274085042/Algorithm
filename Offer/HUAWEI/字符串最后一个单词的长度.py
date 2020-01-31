#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.

'''
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。
'''
#str.split()函数默认可以按空格分割，并且把结果中的空字符串删除掉，留下有用信息

str=input()
str_list=str.split()
last=str_list[-1]
length=len(last)
print(length)
