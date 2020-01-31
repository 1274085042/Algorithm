#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组
'''
str1=input()
str2=input()

def output(str):
    res=[]
    l=len(str)
    if l>8:
        div=l//8
        mod=l%8
        for j in range(div):
            res.append(str[0+8*j:8+8*j])
        if mod!=0:
            res.append(str[l-mod:]+(8-mod)*'0')
        else:
            pass

    elif 0<l<8:
        str=str+(8-l)*'0'
        res.append(str)
    elif l==8:
        res.append(str)
    else:
        pass

    for s in res:
        print( s )
output(str1)
output(str2)
