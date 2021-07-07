#coding=utf-8

'''
题目描述
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。
下面是它的工作原理：首先，选择一个单词作为密匙，如TRAILBLAZERS。
如果单词中包含有重复的字母，只保留第1个，其余几个丢弃。
现在，修改过的那个单词属于字母表的下面，如下所示：

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

T R A I L B Z E S C D F G H J K M N O P Q U V W X Y

上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，
信息中的每个字母被固定于顶上那行，并用下面那行的对应字母一一
取代原文的字母(字母字符的大小写状态应该保留)。
因此，使用这个密匙，Attack AT DAWN(黎明时攻击)就会被加密为
Tpptad TP ITVH。
请实现下述接口，通过指定的密匙和明文得到密文。
详细描述：
接口说明
原型：
voidencrypt(char * key,char * data,char * encrypt);
输入参数：
char * key：密匙
char * data：明文
输出参数：
char * encrypt：密文
返回值：
void
输入描述:
先输入key和要加密的字符串
输出描述:
返回加密后的字符串
'''

def solution(key,data):
    encrypt=[]
    dic=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    key_l=list(key)
    #去重
    key_quchong=[]
    for i in key_l:
        if i not in key_quchong:
            key_quchong.append(i)
    for j in dic:
        if j.lower() not in key_quchong and j.upper() not in key_quchong:
            key_quchong.append(j)
    #print(key_quchong)

    data_l=data.split()
    for str in data_l:
        res=[]
        for ind in range(len(str)):
            index=dic.index(str[ind].upper())
            if str[ind].islower():
                res.append(key_quchong[index].lower())
            else:
                res.append(key_quchong[index])

        encrypt.append("".join(res))

    return " ".join(encrypt)

while True:
    try:
        key=input().strip()
        data=input().strip()
        print(solution(key,data))
    except:
        break