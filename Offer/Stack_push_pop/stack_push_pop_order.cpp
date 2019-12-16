/*
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1，2，3，4，5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
*/

#include <stack>
#include <vector>
#include <iostream>

using namespace std;

bool IsPopOrder(vector<int> pushV,vector<int> popV)
{
    bool res=false;
    auto popnext=popV.begin();
    auto pushnext=pushV.begin();
    stack<int> st;                      //辅助栈

    if (pushV.empty() || popV.empty())
    {
        return res;
    }

    while (popnext!=popV.end())
    {
       if (st.empty())
       {
           st.push(*pushnext);
           ++pushnext;
       }
       while (st.top()!=*popnext && pushnext!=pushV.end())
       {
           st.push(*pushnext);
           ++pushnext;
       }
       if(st.top()!=*popnext)
       {
           break;
       }
       else
       {
           st.pop();
           ++popnext;
       }
       
      
    }

    if (st.empty() && popnext==popV.end())
    {
        res=true;
    }

    return res;

}

int main()
{
    vector <int> pushorder={1,2,3,4,5};
    vector <int> poporder1={4,5,3,2,1};
    vector <int> poporder2={4,3,5,1,2};
    /*
    for(auto i=a.begin();i!=a.end();i++)
    {
        cout<<*i<<endl;
    }
    */
   cout<<IsPopOrder(pushorder,poporder2)<<endl;
    system("pause");
    return 0;
}