/*
 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。 
*/


struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(nullptr), right(nullptr) {
	}
};

class Solution {
public:
    void Convert(TreeNode* root,TreeNode ** pLastNode)
    {
        if (root==nullptr)
        {
            return ;
        }
        TreeNode *current=root;
        if(current->left!=nullptr)
            Convert(current->left,pLastNode);

        current->left=*pLastNode;

        if(*pLastNode!=nullptr)
            (*pLastNode)->right=current;

        *pLastNode=current;

        if (current->right!=nullptr)
        {
            Convert(current->right,pLastNode);
        }
        

    }
    TreeNode* Convert(TreeNode* pRootOfTree)
    {
     TreeNode *pLastNode=nullptr;
     Convert(pRootOfTree,&pLastNode);  //要想pLastNode的地址有所改变，在Convert中就要传递pLastNode的地址
     TreeNode *pHeadNode=pLastNode;
     while (pHeadNode!=nullptr && pHeadNode->left!=nullptr)
     {
         pHeadNode=pLastNode->left;
     }
     return pHeadNode;
    }
};