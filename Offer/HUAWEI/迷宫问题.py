#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
定义一个二维数组N*M（其中2<=N<=10;2<=M<=10），如5 × 5数组下所示：
int maze[5][5] = {
        0, 1, 0, 0, 0,
        0, 1, 0, 1, 0,
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 0,
        0, 0, 0, 1, 0,
};

它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，
要求编程序找出从左上角到右下角的最短路线。入口点为[0,0],既第一空格是可以走的路。

Input
一个N × M的二维数组，表示一个迷宫。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
Output
左上角到右下角的最短路径，格式如样例所示。

Sample Input
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0

Sample Output
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(3, 4)
(4, 4)
输入描述:
输入两个整数，分别表示二位数组的行数，列数。再输入相应的数组，其中的1表示墙壁，0表示可以走的路。
数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。

输出描述:
左上角到右下角的最短路径，格式如样例所示。
'''
def MiGong(mat,rows,columns):
    temp=[]
    for i in range(rows):
        for j in range(columns):
            if mat[i][j]==0:
                temp.append([i,j])
    res=search(temp,rows,columns)
    #print(res)
    return  res


def search(temp,rows,columns):
    res=[[0,0]]
    for t in temp[1:]:
        if t[0]-res[-1][0]==1 and t[1]-res[-1][1]==0:
            res.append(t)
        elif t[0]-res[-1][0]==0 and t[1]-res[-1][1]==1:
            res.append(t)
    if res[-1]!=[rows-1,columns-1]:
        #print(res)
        temp.remove(res[-1])
        #print(temp)

        return  search(temp,rows,columns)

    else:
        #print(res)
        return res



while True:
    try:
        rows,columns=list(map(int,input().strip().split()))
        mat=[list(map(int,input().strip().split())) for i in range(rows)]
        res=MiGong(mat,rows,columns)
        for i in res:
            print('({},{})'.format(i[0],i[1]))

    except:
        break


