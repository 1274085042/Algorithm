#coding=utf-8
'''
题目描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形

说明：
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，
则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

输入描述:
整数N

输出描述:
最少需要几位同学出列
'''

import bisect

def solution(l):
    res=[]
    assist_l=[9999]*len(l)
    for i in range(len(l)):
        pos=bisect.bisect_left(assist_l,l[i])  #查找当前值在辅助列表中的位置
        res.append(pos+1)
        assist_l[pos]=l[i]
    return res


while True:
    try:
        n=int(input().strip())
        #n=8
        # l=[186,186,150,200,160,130,197,200]
        l=list(map(int,input().strip().split()))


        forward_l=solution(l)  #forward_l 存储列表正向遍历时，以当前值结尾的最长递增序列的长度
        backward_l=solution(l[::-1])  #backward_l 存储列表反向遍历时，以当前值结尾的最长递增序列的长度。

        backward_l=backward_l[::-1]   #存储了原列表中每个值开头的最长递减序列的长度

        k=max([forward_l[i]+backward_l[i] for i in range(len(l))])-1

        print(n-k)
    except:
        break
