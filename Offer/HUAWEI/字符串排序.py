#coding=utf-8

'''
题目描述
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y

输入描述:
输入字符串
输出描述:
输出字符串
'''

alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
def str_sort(str):
    str_lower=str.lower()
    str_list_ori=list(str)
    str_list_new=str_list_ori.copy()
    str_lowerlist=list(str_lower)
    res=[]
    for i in range(len(str_list_ori)):
        if 'a'<=str_list_ori[i]<='z' or 'A'<=str_list_ori[i]<='Z':
            for j in alphabet:
                if j in str_lowerlist:

                    res.append(str_list_new[str_lowerlist.index(j)])
                    str_list_new.remove( str_list_new[str_lowerlist.index( j )] )
                    str_lowerlist.remove(j)

                    break

        else:
            res.append(str_list_ori[i])

    return "".join(res)

while True:
    try:
        str=input().strip()
        print(str_sort(str))
    # str1='A Famous Saying: Much Ado About Nothing (2012/8).'
    # str2='By?e'
    # str3='BabA'
    # print(str_sort(str1))
    # print(str_sort(str2))
    # print(str_sort(str3))
    except:
        break
