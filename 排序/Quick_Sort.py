#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.


def Quick_Sort(arr):
    if len( arr ) >= 2:                         #递归终止的条件
        pivot=arr[0]                            #选取基准
        #定义基准左右两侧的列表
        left=[]
        right=[]

        for i in arr[1:]:
            if i>=pivot:
                right.append(i)
            else:
                left.append(i)
        return Quick_Sort(left)+[pivot]+Quick_Sort(right)
    else:
        return arr

arr1=[2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
arr2=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
arr3 = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(Quick_Sort(arr1))
print(Quick_Sort(arr2))
print(Quick_Sort(arr3))