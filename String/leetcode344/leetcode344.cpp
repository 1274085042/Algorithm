#include <vector>
#include <iostream>
using namespace std;

class Solution 
{
public:
    void reverseString(vector<char>& s) 
    {
        int i, j;
        for (i = 0, j = s.size() - 1; i <s.size()/2; ++i, --j)
        {
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
        }
    }
};

int main()
{
    vector<char> v = { 'H','a','n','n','a','h'};
    Solution sol;
    sol.reverseString(v);
    copy(v.begin(), v.end(), ostream_iterator<char>(cout, " "));
}