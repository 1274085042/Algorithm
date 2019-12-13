#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，是得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和
偶数之间的相对位置不变。
'''

class Solution():
    def reOrderArray(self,array):
        odd=[]
        even=[]
        for i in array:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)

        return odd+even

s=Solution()
print(s.reOrderArray([2,4,21,1,3,4]))