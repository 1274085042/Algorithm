/*
从下往上打印二叉树的每个节点，同层节点从左至右打印
*/

#include <vector>
#include <deque>
#include <iostream>

using namespace std;

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(nullptr), right(nullptr) {
	}
};


vector<int> PrintFromTopToBottom(TreeNode* root) 
{
    vector <int> v;
    if (root==nullptr)
    {
        return v;
    }
    else
    {
        deque<TreeNode *> deq;   //辅助队列
        deq.push_front(root);
        
        while (deq.size())
        {
            TreeNode *t=deq.front();
            deq.pop_front();
            v.push_back(t->val);
            if (t->left)
            {
                deq.push_back(t->left);
            }
            if (t->right)
            {
                deq.push_back(t->right);
            }
        } 
        return v;  
    }  

}


/**
 *容器有：序列容器、关联容器 
 * 序列容器：list、vector、queue、deque、stack
 */