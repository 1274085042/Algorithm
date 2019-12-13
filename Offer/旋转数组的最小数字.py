#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
输入一个非递减排序数组的一个旋转，输出该旋转数组的最小元素
'''
class Solution:
    def minNumberInRotateAr(self,rotateArray):
        if len(rotateArray)==0:
            return 0
        elif len(rotateArray)==1:
            return rotateArray[0]
        else:
            return min(rotateArray)

l=[3,4,5,1,2]
s=Solution()
print(s.minNumberInRotateAr(l))

