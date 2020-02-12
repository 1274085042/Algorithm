#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
1、对输入的字符串进行加解密，并输出。
2、加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。
接口描述：
实现接口，每个接口实现1个基本操作：
void Encrypt (char aucPassword[], char aucResult[])：在该函数中实现字符串加密并输出
说明：
1、字符串以\0结尾。
2、字符串最长100个字符。
int unEncrypt (char result[], char password[])：在该函数中实现字符串解密并输出
说明：
1、字符串以\0结尾。
2、字符串最长100个字符。
'''

def Encrypy(str,res):

    for i in range(len(str)):
        if 'a'<=str[i]<='z' or 'A'<=str[i]<='Z':
            if str[i].islower():
                c=str[i].upper()
            else:
                c=str[i].lower()

            if c=='z':
                c='a'
            elif c=='Z':
                c='A'

            else:
                ascii=ord(c)
                c=chr(ascii+1)

            res.append(c)

        elif  '0'<=str[i]<='9':
            if str[i]=='9':
                c='0'
            else:
                ascii=ord(str[i])
                c=chr(ascii+1)
            res.append(c)

        else:
            res.append(str[i])

    return  "".join(res)


def unEncrypt(str,res):
    for i in range(len(str)):
        if 'a'<=str[i]<='z' or 'A'<=str[i]<='Z':
            if str[i].islower():
                c=str[i].upper()
            else:
                c=str[i].lower()

            if c=='a':
                c='z'
            elif c=='A':
                c='Z'

            else:
                ascii=ord(c)
                c=chr(ascii-1)

            res.append(c)

        elif  '0'<=str[i]<='9':
            if str[i]=='0':
                c='9'
            else:
                ascii=ord(str[i])
                c=chr(ascii-1)
            res.append(c)

        else:
            res.append(str[i])

    return  "".join(res)

while True:
    try:
        # str1="abcdefg129"
        # res1=[]
        #
        # str2="BCDEFGH230"
        # res2=[]
        str1=input()
        str2=input()
        res1=[]
        res2=[]

        print(Encrypy(str1,res1))
        print(unEncrypt(str2,res2))

    except:
        break
