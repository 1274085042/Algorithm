#include <iostream>
#include <string>

using namespace std;

class Solution 
{
public:
    string reverseStr(string s, int k) 
    {
        for (int i = 0; i < s.size(); i += (2 * k))
        {
            if (i + k <= s.size())
            {
                reverse(s.begin()+i,s.begin()+k+i);
            }
            else
            {
                reverse(s.begin() + i,s.begin()+s.size());
            }
        }
        return s;
    }
};

int main()
{
    string s = "abcdefg";
    Solution sol;
    s= sol.reverseStr(s, 2);
    cout << s << endl;
}