#coding=utf-8

'''
题目描述

若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，
例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，
而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，
当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。

输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。
'''

def prime_judge(n):
    m=int(n**0.5)  #如果一个数能被因数分解，那么分解的两个输一个小于等于n**0.5,一个大于等于n**0.5
    for i in range(2,m+1):
        if n%i==0:
            return False

    return True


def odd_even(l):

    even=[]
    odd=[]
    for i in l:
        if int(i)%2==0:
            even.append(int(i))
        else:
            odd.append(int(i))

    return even,odd

def matrix_prime(even,odd):
    mat=[[0 for i in range(len(even))] for j in range(len(odd))]
    for ii,i in enumerate(odd):
        for jj,j in enumerate(even):
            if prime_judge(i+j):
                mat[ii][jj]=1
    return mat



def find(x):
    for index, i in enumerate( even ):
        if mat[x][index] == 1 and used[index] == 0:
            used[index] = 1
            if connect[index] == -1 or find( connect[index] ) != 0:
                connect[index] = x
                return 1
    return 0


while True:
    try:
        #n = 4
        #m = ["2","5","6","13"]
        n=int(input())
        m=input().strip().split()
        even,odd = odd_even( m )
        mat=matrix_prime(even,odd)
        print(mat)
        connect = [-1 for i in range( len( even ) )]
        count = 0
        for i in range( len( odd ) ):
            used = [0 for j in range( len( even) )]
            if find( i ):
                count += 1
        print( count )
    except:
        break