#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）

最后一个数后面也要有空格

详细描述：

函数接口说明：

public String getResult(long ulDataInput)

输入参数：

long ulDataInput：输入的正整数

返回值：

String

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。
'''

num=int(input())
def qiuzhishu(x):
    res=''
    for i in range(2,x+1):   #从2开始
        while(x%i==0):       #每找到一个因数，除尽为止。找到的因数一定是质数
            res=res+str(i)+' '
            x=x/i

    print(res)

qiuzhishu(num)







