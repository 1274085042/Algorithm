#include <vector>
#include <iostream>
using namespace std;

class Solution 
{
public:
    int climbStairs(int n) 
    {
        if (n <= 1)
        {
            return 1;
        }
        vector<int> dp(n + 1);
        dp[1] = 1;
        dp[2] = 2;
        if (n <= 2)
        {
            return dp[n];
        }
        else
        {
            for (int i = 3; i <= n; ++i)
            {
                dp[i] = dp[i - 1] + dp[i - 2];
            }
        }
        return dp[n];
    }
};

int main()
{
    Solution sol;
    cout << sol.climbStairs(4) << endl;
}


/*
一步一个台阶，两个台阶，三个台阶，直到 m个台阶，有多少种方法爬到n阶楼顶。

class Solution 
{
public:
    int climbStairs(int n) 
    {
        int m = 2;

        if (n <= 1)
        {
            return 1;
        }
        vector<int> dp(n + 1);
        dp[0] = 1;

        for(int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= m; ++j)
            {
                if (i - j >= 0)
                {
                    dp[i] += dp[i - j];
                }
            }
        }
        return dp[n];
    }
};
*/
