#coding=utf-8

'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def DoesTree1hasTree2(self, pRoot1, pRoot2):
        if pRoot2==None:
            return True

        if pRoot1==None:
            return False

        if pRoot1.val!=pRoot2.val:
            return False

        else:
            return self.DoesTree1hasTree2(pRoot1.left, pRoot2.left) and self.DoesTree1hasTree2(pRoot1.right, pRoot2.right)


    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res=False

        if pRoot1==None:
            return False
        if pRoot2==None:
            return False

        if pRoot1.val==pRoot2.val:
            res=self.DoesTree1hasTree2(pRoot1,pRoot2)

        if res==False:
            res=self.HasSubtree( pRoot1.left, pRoot2)

        if res==False:
            res = self.HasSubtree(  pRoot1.right, pRoot2 )
        return res