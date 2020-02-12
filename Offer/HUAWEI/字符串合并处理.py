#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
按照指定规则对输入的字符串进行处理。

详细描述：
将输入的两个字符串合并。
对合并后的字符串进行排序，要求为：下标为奇数的字符和下标为偶数的字符分别从小到大排序。
这里的下标意思是字符在字符串中的位置。
对排序后的字符串进行操作，如果字符为‘0’——‘9’或者‘A’——‘F’或者‘a’——‘f’，
则对他们所代表的16进制的数进行BIT倒序的操作，并转换为相应的大写字符。如字符为‘4’，为0100b，则翻转后为0010b，也就是2。
转换后的字符为‘2’； 如字符为‘7’，为0111b，则翻转后为1110b，也就是e。转换后的字符为大写‘E’。
举例：输入str1为"dec"，str2为"fab"，合并为“decfab”，分别对“dca”和“efb”进行排序，排序后为“abcedf”，转换后为“5D37BF”
接口设计及说明：
/*
功能:字符串处理
输入:两个字符串,需要异常处理
输出:合并处理后的字符串，具体要求参考文档
返回:无
*/
void ProcessString(char* str1,char *str2,char * strOutput)
{
}

'''


def str_merge(str_list):
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    res = []
    for s in str_list:
        if s.upper() in dic:
            ind=int(bin(dic.index(s.upper())).replace("0b","").rjust(4,"0")[::-1],2)
            res.append(dic[ind])
        else:
            res.append(s)
    return "".join(res)

def get_input():
    #s=list("dec fabh".replace(" ",""))
    s = list(input().strip().replace( " ", "" ) )
    odd=[]
    even=[]
    res=[]
    for i,v in enumerate(s):
        if i%2==0:
            even.append(v)
        else:
            odd.append(v)

    even.sort()
    odd.sort()
    l=len(even)
    for j in range(l):
        res.append(even[j])
        try:
            res.append(odd[j])
        except:
            break

    return res
while True:
    try:
        str_list=get_input()
        print(str_merge(str_list))
    except:
        break
