#coding=utf-8

'''
题目描述：
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

输入描述:
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述:
输出输入字符串中含有该字符的个数。
'''

str=input()
c=input()
if c.isupper():
    times1=str.count(c)
    c=c.lower()
    times2=str.count(c)
    times=times1+times2
elif c.islower():
    times1=str.count(c)
    c=c.upper()
    times2=str.count(c)
    times=times1+times2
else:
    times=str.count(c)
print(times)