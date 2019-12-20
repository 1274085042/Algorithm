/*
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
*/
#include <vector>
#include <iterator>

using namespace std;

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(nullptr), right(nullptr) {
	}
};

void FindPath(TreeNode* root,int expectsum,vector <int> path,int sum,vector <vector<int>> &v);

vector <vector<int>> FindPath(TreeNode* root,int expectNumber) 
{
 
   //vector <vector<int>> vec;
        vector <vector<int>> res;
        vector <int> path;          //从树根到树叶的路径
        int sum=0;
        if (root==nullptr)
        {
            return res;
        }
        else
        {
           FindPath(root,expectNumber,path,sum,res);
           return res;
        }
}

void FindPath(TreeNode* root,int expectsum,vector <int> path,int sum,vector <vector<int>> &v)
{
    path.push_back((*root).val);
    sum+=(*root).val;

    if(sum==expectsum && (*root).left==nullptr && (*root).right==nullptr)   //如果路径中的和等于期望值，并且最后一个节点是叶子节点
    {
        v.push_back(path);
    }
    else
    {
        if((*root).left!=nullptr)
        {
            FindPath(root->left,expectsum,path,sum,v);
        }
        if((*root).right!=nullptr)
        {
            FindPath(root->right,expectsum,path,sum,v);
        }
    }
    //path.pop_back();   
}