#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
密码要求:

1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复

说明:长度超过2的子串

输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG
'''

def check_len(str):
    if len(str)>8:
        return  True
    else:
        return  False

def check_type(str):
    lower=False
    capital=False
    digital=False
    other=False

    str_list=list(str)
    for i in str_list:
        if '0'<=i<='9':
            digital=True
        elif 'a'<=i<='z':
            lower=True
        elif 'A'<=i<='Z':
            capital=True
        else:
            other=True
    if (lower and capital and digital)==True:
        return True
    elif (lower and capital and other) ==True:
        return True
    elif (lower and digital and other) ==True:
        return True
    elif (capital and digital and other) ==True:
        return True
    else:
        return False

def check_repeat(str):
    # str_list=list(str)
    # for i in range(len(str_list)):
    #     #rstr=str_list.remove(str_list[i:i+3])
    #     rstr=str_list[:i]+str_list[i+3:]
    #     if i+3<len(str_list):
    #         if ''.join(str_list[i:i+3]) in ''.join(rstr):
    #             return False
    for i in range(len(str)-3):
        if str[i:i+3] in str[i+1:]:
            return False
    return  True

while True:
    try:
        str=input().strip()
        if check_len(str) and check_type(str) and check_repeat(str):
            print('OK')
        else:
            print('NG')
    except:
        break
