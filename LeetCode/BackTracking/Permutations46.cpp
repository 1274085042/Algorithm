#include <vector>
#include <iostream>
#include <iterator>

using namespace std;

class Solution
{
public:
  vector<vector<int>> Permute(vector<int> &nums)
  {
    BackTrack(nums, 0);
    return permutations_;
  }

private:
  vector<vector<int>> permutations_;
  void BackTrack(vector<int> &nums, int first)
  {
    if (first == (nums.size() - 1) /*递归终止*/)
    {
      permutations_.emplace_back(nums);
      return;
    }
    for (int i = first; i < nums.size(); ++i)
    {
      swap(nums[first], nums[i]);
      BackTrack(nums, first + 1); // 递归
      swap(nums[first], nums[i]); // 回溯
    }
  }
};

int main()
{
  vector<int> nums{1, 2, 3};
  auto solution = Solution();
  auto res = solution.Permute(nums);
  for (const auto &v : res)
  {
    copy(v.begin(), v.end(), ostream_iterator<int>(std::cout, " "));
    cout << endl;
  }
}