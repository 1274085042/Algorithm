#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

int LengthofLongestSubstring(string &s) {
  if (s.length() == 0) {
    return 0;
  }
  int startIndex = 0;
  int currentLength = 0;
  int maxLength = 0;
  unordered_map<char, int> hashTable;  
  for(int i=0; i<s.length(); i++){
    // hashTable记录了当前字符s[i]之前的unique character
    if(hashTable.find(s[i]) == hashTable.end()) {   
      //当前滑动窗口中的字符还没出现重复
      currentLength +=1;
      hashTable[s[i]] = i;
    } else {
      if(currentLength > maxLength) {
        maxLength = currentLength;
      }
      /*
      *【滑动窗口的移动和收缩】
      * 如果hashTable[s[i]] > startIndex，说明当前滑动窗口中的子串出现了重复字符
      * 否则当前滑动窗口中的子串没有出现重复字符
      */
      startIndex = max(hashTable[s[i]], startIndex);
      currentLength = i - startIndex;
      hashTable[s[i]] = i; // 更新unique character的下标  
    }

  }
  if (currentLength > maxLength) {
    maxLength = currentLength;
  }
  return maxLength;
}

int main() {
  string s = "pcwwkecab";
  int res = LengthofLongestSubstring(s);
  cout<<res<<endl;
}