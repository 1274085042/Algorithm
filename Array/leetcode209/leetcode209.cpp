#include <vector>
#include <iostream>

using namespace std;

class Solution 
{
public:
    int minSubArrayLen(int target, vector<int>& nums) 
    {
        int result = INT32_MAX;
        int i = 0;   //子数组的开始位置
        int subLength = 0;
        int sum = 0;
        for(int j = 0; j<nums.size(); ++j)  
        {
            sum += nums[j];

            while(sum>= target)
            {
                subLength = j - i + 1;
                result = result > subLength? subLength : result;
                sum-=nums[i++];
            }
        }

        if(result == INT32_MAX)
        {
            return 0;
        }

        return result;
    }
};

int main()
{
    vector<int> nums1= {2,3,1,2,4,3};
    vector<int> nums2= {1,4,4};
    vector<int> nums3= {1,1,1,1,1,1,1,1};

    Solution sol;
    cout<<sol.minSubArrayLen(7, nums1)<<endl;
    cout<<sol.minSubArrayLen(4, nums2)<<endl;
    cout<<sol.minSubArrayLen(11, nums3)<<endl;
}