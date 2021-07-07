#coding=utf-8

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果都不含重复的数字。
请重建该二叉树并返回。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre)==0:
            return  None
        elif len(pre)==1:
            root=TreeNode(pre[0])
            return root
        else:
            '''
            前序遍历：根节点，左子树，右子树
            中序遍历：左子树，根节点，右子树
            '''
            root=TreeNode(pre[0])
            root.left=self.reConstructBinaryTree(pre[1:tin.index(root.val)+1],tin[:tin.index(root.val)])
            root.right=self.reConstructBinaryTree(pre[tin.index(root.val)+1:],tin[tin.index(root.val)+1:])

            return root
