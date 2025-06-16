#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

/*
 * - 任何数和0做异或运算，结果是原来的数
 * - 任何数和自身做异或运算，结果是0
 * - 异或运算满足交换律和结合律
 */
int SingleNumber(vector<int> &nums)
{
  int res = 0;
  for (const auto &num : nums)
  {
    res ^= num;
  }
  return res;
}
