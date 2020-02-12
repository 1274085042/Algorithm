#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.

'''
题目描述
对字符串中的所有单词进行倒排。

说明：

1、每个单词是以26个大写或小写英文字母构成；

2、非构成单词的字符均视为单词间隔符；

3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；

4、每个单词最长20个字母；
'''
# while True:
#     try:
#          sentence = "$bo*y gi!r#l #".strip().split()
#          res = []
#          for str in sentence:
#              l=len(str)
#              new_str=[]
#
#             for i in range(l):
#                 if 'a'<=str[i]<='z' or 'A'<=str[i]<='Z':
#                     new_str.append(str[i])
#                     if i==l-1:
#                         res.append("".join(new_str))
#                 else:
#                     if len(new_str)!=0:
#                         res.append("".join(new_str))
#                         new_str=[]
#         sentence = res[::-1]
#         res = " ".join( sentence )
#         print( res )
#     except:
#         break

while True:
    try:
        sentence = input().strip().split()
        res = []
        for str in sentence:
            l=len(str)
            new_str=[]

            for i in range(l):
                if 'a'<=str[i]<='z' or 'A'<=str[i]<='Z':
                    new_str.append(str[i])
                    if i==l-1:
                        res.append("".join(new_str))
                else:
                    if len(new_str)!=0:
                        res.append("".join(new_str))
                        new_str=[]
        #print(res)
        sentence = res[::-1]
        res = " ".join( sentence )
        print( res )
    except:
        break