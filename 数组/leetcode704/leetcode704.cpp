#include <vector>
#include <iostream>

using namespace std;

class Solution 
{
public:
    int search(vector<int>& nums, int target) 
    {
        return search_help(nums, 0, nums.size()-1, target);
    }

    int search_help(vector<int>& nums, int left, int right, int target) 
    {
        if(left <= right)
        {
            int mid = (right-left)/2 + left;

            if (nums[mid] == target)
            {
                return mid;
            }
            else if(nums[mid] < target)
            {
                return search_help(nums, mid+1, right, target);
            }
            else
            {
                return search_help(nums, left, mid-1, target);
            }
        }
        return -1;
    }
};

int main()
{
    vector<int> nums1={-1,0,3,5,9,12};
    Solution sol;
    cout<<sol.search(nums1, 9)<<endl;

    vector<int> nums2={-1,0,3,5,9,12};
    cout<<sol.search(nums2, 2)<<endl;
}