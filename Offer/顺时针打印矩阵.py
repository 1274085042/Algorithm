#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.

'''
 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵：
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

class Solution():
    def printMatrix(self,matrix):
        #h=matrix.shape[0]
        #w=matrix.shape[1]
        h=len(matrix)
        w=len(matrix[0])

        start=0
        res=[]
        while(2*start<w and 2*start<h):
            res.extend(self.printMatrixNumber(matrix,start,h,w))
            start+=1
        return res
    def printMatrixNumber(self,matrix,start,h,w):
        res=[]
        endX=w-1-start
        endY=h-1-start
        for i in range(start,endX+1):
            #print("从左到右：",matrix[start][i])
            res.append(matrix[start][i])

        if endY>start:
            for j in range(start+1,endY+1):
                #print("从上到下：",matrix[j][endX])
                res.append( matrix[j][endX] )

        if endY>start and endX>start:
            for i in range(endX-1,start-1,-1):
                #print("从右到左：",matrix[endY][i])
                res.append(matrix[endY][i])

        if endY > start and endX > start and endY>start+1:
            for j in range(endY-1,start,-1):
                res.append( matrix[j][start])
                #pint("从下到上：",matrix[j][start])

        return res



import numpy as np
#numbers=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
numbers=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#print(numbers.shape)
s=Solution()
res=s.printMatrix(numbers)
print(res)