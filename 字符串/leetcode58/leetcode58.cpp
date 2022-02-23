#include <iostream>
#include <string>

using namespace std;

class Solution 
{
public:
    string reverseLeftWords(string s, int n) 
    {
        reverse(s.begin(), s.begin() + n);
        reverse(s.begin() + n, s.end());
        reverse(s.begin(), s.end());
        return s;
    }
};

int main()
{
    string str = "abcdefg";
    Solution sol;
    str = sol.reverseLeftWords(str, 2);
    cout << str << endl;
}