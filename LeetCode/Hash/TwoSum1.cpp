#include <vector>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

vector<int> Solution(vector<int> &nums, int target){
  unordered_map<int, int> hash_table;
  for(int i=0; i<nums.size(); i++) {
    int remain = target - nums[i];
    auto it = hash_table.find(remain);
    if(it != hash_table.end()) {
      return {it->second, i};
    } else {
      hash_table[nums[i]] = i;
    }
  }
  return {};
}

int main()
{
  vector<int> nums {2, 10, 7, 11, 15};
  int target = 9;
  auto res = Solution(nums, target);
  copy(res.begin(), res.end(), ostream_iterator<int>(std::cout, " "));
}