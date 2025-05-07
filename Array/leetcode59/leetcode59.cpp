#include <vector>
#include <iostream>

using namespace std;

class Solution 
{
public:
    vector<vector<int>> generateMatrix(int n) 
    {
        vector<vector<int>> res (n, vector<int>(n,0));
        int loop = n/2;                             //表示有几个圈
        int startR = 0;                             //行的起始位置
        int startC = 0;                             //列的起始位置
        int offset = 1;                             //offset计算终止位置

        int mid = n/2;                              //矩阵的中间位置
        int i, j;                           //遍历行和列

        int count = 1;                              //矩阵中填充的数值

        while(loop--)
        {
            i = startR;
            j = startC;

            for(j = startC; j<startC+n-offset; j++) //从左向右
            {
                res[i][j] = count++;
            }

            for(i = startR; i<startR+n-offset; i++) //从上到下
            {
                res[i][j] = count++;
            }

            for(; startC<j; j--)                    //从右到左
            {
                res[i][j] = count++;
            }

            for(; startR<i; i--)                    //从下到上
            {
                res[i][j] = count++;
            }

            startR++;
            startC++;

            offset+=2;
        }

        if(n%2)
        {
            res[mid][mid] = count;
        }

        return res;
    }
};

int main()
{
    Solution sol;
    vector<vector<int>> res1=sol.generateMatrix(3);
    for(auto &v : res1)
    {
        for(auto &i:v)
        {
            cout<<i<<" ";
        }
    }
    cout<<endl;
    vector<vector<int>> res2=sol.generateMatrix(1); 

}