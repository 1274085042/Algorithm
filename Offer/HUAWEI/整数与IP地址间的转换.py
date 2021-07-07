#coding=utf-8

'''
题目描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，
然后把这个二进制数转变成一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。

的每段可以看成是一个0-255的整数，需要对IP地址进行校验
输入描述:
输入
1 输入IP地址
2 输入10进制型的IP地址

输出描述:
输出
1 输出转换成10进制的IP地址b
2 输出转换后的IP地址
'''
def chechip(ip):
    for i in ip:
        if i<0 or i>255:
            return  False
    return True
def ipConvertint(str):
    ip=list(map(int,str.strip().split(".")))
    if chechip(ip):
        ip_B=[]
        for i in ip:
            i_B=bin(i).replace('0b',"").rjust(8,"0")
            ip_B.append(i_B)
        ipB="".join(ip_B)
        ipD=int(ipB,2)
        return ipD
def intConvertip(n):
    ipB=bin(n).replace('0b','').rjust(32,'0')
    ip_list=[]
    for i in range(4):
        ip_list.append(str(int(ipB[8*i:8+8*i],2)))
    # ip=""
    # for j in ip_list:
    #     ip=ip+str(j)+'.'
    # ip=ip[:-1]
    return ".".join(ip_list)


while True:
    try:
        ip=input().strip()
        ipD=int(input().strip())
        print(ipConvertint(ip))
        print(intConvertip(ipD))
    except:
        break

# print(ipConvertint('10.0.3.256'))
# print(intConvertip(167969729))