#coding=utf-8

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root==None:
            return
        if root.left==None and root.right==None:  #说明该节点是叶子节点
            return

        else:
            tmp=root.left
            root.left=root.right
            root.right=tmp
            if root.left!=None:
                self.Mirror(root.left)
            if root.right!=None:
                self.Mirror(root.right)

        return root