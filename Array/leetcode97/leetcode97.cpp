#include <vector>
#include <iostream>

using namespace std;

class Solution 
{
public:
    vector<int> sortedSquares(vector<int>& nums) 
    {
        int k = nums.size() - 1;
        vector<int> res (nums.size(), 0);
        
        int i = 0;
        int j = nums.size() - 1;

        while (i <= j)
        {
            if((nums[i]*nums[i]) > (nums[j]*nums[j]))
            {
                res[k--] = nums[i]*nums[i];
                ++i;
            }
            else
            {
                res[k--] = nums[j]*nums[j];
                --j;
            }

        }

        return res;
    }
};

int main()
{
    vector<int> nums1={-4,-1,0,3,10};
    vector<int> nums2={-7,-3,2,3,11};
    Solution sol;
    vector<int> res1=sol.sortedSquares(nums1);
    for(auto &e:res1)
    {
        cout<<e<<" ";
    }
    cout<<endl;
    vector<int> res2=sol.sortedSquares(nums2);
    for(auto &e:res2)
    {
        cout<<e<<" ";
    }
}