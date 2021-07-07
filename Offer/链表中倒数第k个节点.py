#coding=utf-8

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        lis=[]
        while head!=None:
            lis.append(head)
            head=head.next
        length=len(lis)
        if k>length or k<=0:
            return
        else:
            return lis[length-k]
