#include <vector>
#include <iostream>

using namespace std;

class Solution 
{
public:
    int removeElement(vector<int>& nums, int val) 
    {
        int slowIndex = 0;
        for(int fastIndex = 0; fastIndex < nums.size(); ++fastIndex)
        {
            if(nums[fastIndex] != val)
            {
                nums[slowIndex] = nums[fastIndex];
                ++slowIndex;
            }
        }

        return slowIndex;
    }
};

int main()
{
    vector<int> nums1={3,2,2,3};
    Solution sol;
    cout<<sol.removeElement(nums1, 3)<<endl;

    vector<int> nums2={0,1,2,2,3,0,4,2};
    cout<<sol.removeElement(nums2, 2)<<endl;
}