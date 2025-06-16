#include <vector>
#include <iostream>

using namespace std;

// 累积到当前num时，curSum比当前的元素还小，则丢弃之前的累积和
int MaxSubarry(vector<int> nums)
{
  int maxSum = nums[0];
  int curSum = 0;
  for (const int &num : nums)
  {
    curSum += num;
    if (curSum < num)
    {
      curSum = num;
    }
    if (curSum > maxSum)
    {
      maxSum = curSum;
    }
  }

  return maxSum;
}

int main()
{
  vector<int> v{-2, 1, -3, 4, -1, 2, 1, -5, 4};
  int res = MaxSubarry(v);
  cout << res << endl;
}