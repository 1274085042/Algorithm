#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。
比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214。因为截获的串太长了，
而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer的工作量实在是太大了，
他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

输入描述:
输入一个字符串

输出描述:
返回有效密码串的最大长度
'''
#方法一：算法复杂度过大
# def LongestPlalindrome(str):
#     longest=0
#     res=""
#     for i in range(len(str)):
#         if i+2<=len(str):
#             for j in range(i+2,len(str)+1):
#                 if str[i:j]==str[i:j][::-1]:
#                     if j-i>longest:
#                         longest=j-i
#                         res=str[i:j]
#     return  res
#
# while True:
#     try:
#         str=input().strip()
#         res=LongestPlalindrome(str)
#         print(len(res))
#     except:
#         break

#方法二：中心扩展

def LongestPlalindrome(str):
    str_list=list(str)
    new_str=[]
    for i in str_list:
        new_str.append('#')
        new_str.append(i)
    new_str.append('#')
    longest=0
    res=[]
    #print(new_str)
    for j in range(1,len(new_str)-1):
        m=j-1
        n=j+1
        while m>=0 and n<len(new_str):
            if new_str[m]==new_str[n]:
                if n-m>longest:
                    longest=n-m
                    res=new_str[m:n+1]
                m-=1
                n+=1
            else:
                break

    print(int((len(res)-1)/2))

# LongestPlalindrome('ABAKK')
# LongestPlalindrome('51233214')
while True:
    try:
        str=input().strip()
        LongestPlalindrome(str)
    except:
        break