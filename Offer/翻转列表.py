#coding=utf-8

'''
输入一个链表，翻转链表后，输出新链表的表头
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        last=None    #翻转后的表头
        while pHead:
            tmp=pHead.next
            pHead.next=last
            last=pHead
            pHead=tmp
        return last
