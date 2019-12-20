/*
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
*/
#include <vector>
#include <iostream>

using namespace std;

bool VerifysequenceofBST (vector <int> sequence)
{
    vector <int> left;
    vector <int> right;

    if (sequence.size()==0)
    {
        return false;
    }
    auto start=sequence.begin();    //序列头指针
    auto end=sequence.end();        
    int root=*(end-1);
    while (start<(end-1))            //二叉搜索树左子树小于根节点
    {
        if(*start>root)
            break;
        else
        {
            left.push_back(*start);
        }
        
        start+=1;
    }
    while (start<(end-1))       //二叉搜索树右子树大于根节点
    {
        if(*start<root)
        {
            return false;
        }
        else
        {
            right.push_back(*start);
        }
        
        start+=1;
    }
    bool l=true;
    if (left.size()!=0)
    {
        l=VerifysequenceofBST(left);
    }

    bool r=true;
    if(right.size()!=0)
    {
        r=VerifysequenceofBST(right);
    }
    return l&&r;
    
}


int main()
{
    //vector <int> v1={1,2,3,4,5};
    //auto i=v1.end();
    //cout<<*(i-1)<<endl;
    vector <int> s1={5,7,6,9,11,10,8};
    vector <int> s2={7,4,6,5};
    bool res1=VerifysequenceofBST(s1);
    bool res2=VerifysequenceofBST(s2);
    cout<<res1<<'\n'<<res2<<endl;
    system("pause");
    return 0;

}