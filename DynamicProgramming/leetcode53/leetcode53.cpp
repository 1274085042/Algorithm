#include <vector>
#include <iostream>

using namespace std;

class Solution 
{
public:
    int maxSubArray(vector<int>& nums) 
    {
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        int res = dp[0];
        for (int i = 1; i < nums.size(); ++i)
        {
            dp[i] = (dp[i - 1] + nums[i])>nums[i]? (dp[i - 1] + nums[i]): nums[i];
            if (dp[i] > res)
            {
                res = dp[i];
            }
        }

        return res;
    }
};

int main()
{
    Solution sol;
    vector<int> v = { -2,1,-3,4,-1,2,1,-5,4 };
    cout << sol.maxSubArray(v) << endl;

}