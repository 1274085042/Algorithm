#coding=utf-8

'''
题目描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255

私网IP范围是：

10.0.0.0～10.255.255.255

172.16.0.0～172.31.255.255

192.168.0.0～192.168.255.255

子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。
'''

A=0
B=0
C=0
D=0
E=0
err=0
pri=0
lll=['254','252','248','240','224','192','128','0']

def check_ip(ip):
     if len(ip)==4 and ''not in ip:
         for i in ip:
             if int(i)<0 or int(i)>255:
                 return False
         return True
     else:
         return  False
def check_mask(ms):
    if ms[0]=='255':
        if ms[1]=='255':
            if ms[2]=='255':
                if ms[3] in lll:
                    return True
                else:
                    return False
            elif ms[2]in lll and ms[3]=='0':
                return True
            else:
                return  False
        elif ms[1] in lll and ms[2]=='0' and ms[3]=='0':
            return True
        else:
            return False
    elif ms[0] in lll and ms[1]==0 and ms[2]==0 and ms[3]==0:
        return True
    else:
        return False


while True:
    str=input().strip()
    #str="1.0.0.1~255.0.0.0"
    if str=='':
        break
    ip,ms=str.split("~")
    ip_list=ip.split('.')
    ms_list=ms.split('.')
    # print(ip_list)
    # print(check_ip(ip_list))
    # # print(check_mask(ms_list))
    # #print(ip,ms)
    # print(check_ip(ip_list))
    # print(check_mask(ms_list))
    if check_ip(ip_list) and check_mask(ms_list):
        if 1<=int(ip_list[0])<=126:
            A+=1
            if int( ip_list[0] ) == 10:
                pri+=1
        elif 128<=int(ip_list[0])<=191:
            B+=1
            if int(ip_list[0])==172 and 16<=int(ip_list[1])<=31:
                pri+=1
        elif 192<=int(ip_list[0])<=223:
            C+=1
            if int(ip_list[0])==192 and int(ip_list[1])==168:
                pri+=1
        elif 224<=int(ip_list[0])<=239:
            D+=1
        elif 240<=int(ip_list[0])<=255:
            E+=1

    else:
        err+=1
print("%d %d %d %d %d %d %d"%(A,B,C,D,E,err,pri))