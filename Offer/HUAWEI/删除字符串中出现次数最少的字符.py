#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。
'''

def check_len(str):
    if len(str)<=20:
        return True
    else:
        return False

def str_delete(str):

    str_list=list(str)
    str_dict={}
    for i in range(len(str)):
        if str[i] not in str_dict.keys():
            str_dict[str[i]]=str.count(str[i])
    m=min(str_dict.values())
    for k,v in str_dict.items():
        if v==m:
            for i in str_list:
                if i==k:
                    str_list.remove(i)
    return "".join(str_list)

while True:
    try :
        str = input().strip()
        if not check_len(str):
            continue
        else:
            print(str_delete(str))

    except:
        break