#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：

如22：twenty two，123：one hundred and twenty three。

说明：
数字为正整数，长度不超过九位，不考虑小数，转化结果为英文小写；
输出格式为twenty two；
非法数据请返回“error”；
关键字提示：and，billion，million，thousand，hundred。
方法原型：public static String parse(long num)
输入描述:
输入一个long型整数
0
输出描述:
输出相应的英文写法
'''

def Solution(n):
    dic1=[ 'one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    dic2=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    dic3 = ['thousand','million']
    res=[]
    n=str(n)
    if len(n)>9 or int(n)<0:
        return "error"
    elif int(n)==0:
            return ''
    else:
        n=int(n)
        if n<20:
            return dic1[n-1]
        elif n<100:
            return dic2[n//10-2]+' '+Solution(n%10)
        elif n<1000:
            tem=Solution(n%100)
            if tem!='':
                return Solution(n//100)+' hundred and '+tem
            else:
                return Solution(n//100)+' hundred'
        else:

            if n<1000000:
                return Solution(n//1000)+' thousand '+Solution(n%1000)
            else:
                return Solution(n//1000000)+' million '+Solution(n%1000000)

while True:
    try:
        n=input()
        print(Solution(n))
# n='123456789'
# print(Solution(n))
    except:
        break