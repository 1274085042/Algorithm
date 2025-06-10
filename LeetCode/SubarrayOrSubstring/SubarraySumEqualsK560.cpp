#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

// 方法1
// int SubarrarySum(vector<int> &nums, int k) {
//   int subarrary_nums = 0;
//   int len = nums.size();
//   int target = k;
//   for(int start=0; start<len; start++) {
//     target = k;
//     for (int end=start; end<len; end++) {
//       target = target - nums[end];
//       if (target==0) {
//         subarrary_nums += 1;
//       }
//     }
//   }
//   return subarrary_nums;
// }

/*方法2
* 滑动窗口（前缀和） 哈希表
*
* 滑动窗口：
    窗口的终止位置为i
    窗口的e起始位置为j
  窗口内数组pre[j..i]的和为pre[i] - pre[j-1]，判断pre[i] - pre[j-1]==k

  使用哈希表unordered_map存储pre[j-1]，初始值为{（0，1）}
*/
int SubarrarySum(vector<int> &nums, int k) {

  int subarrary_count = 0;
  unordered_map<int, int> pre_sum_map{{0,1}}; // key为前缀和，value为前缀和出现的次数
  int pre = 0;

  for(auto & num : nums) {
    pre += num;
    if(pre_sum_map.find(pre-k) != pre_sum_map.end()) {
      subarrary_count += pre_sum_map[pre-k];
    }
    pre_sum_map[pre]++;
  }

  return subarrary_count;
}

int main() {
  // vector<int> v1 = {1,-1,0};
  vector<int> v2 =  {28,54,7,-70,22,65,-6};
  // int res1 = SubarrarySum(v1, 0);
  int res2 = SubarrarySum(v2, 100);
  // cout<<res1<<endl;
  cout<<res2<<endl;
}