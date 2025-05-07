#include <iostream>
#include <string>

using namespace std;

class Solution 
{
public:
    int expend(string &s, int i, int j)
    {
        int res = 0;
        while (i >= 0 && j < s.size()&& s[i] == s[j])
        {
            --i;
            ++j;
            ++res;
        }
        return res;
    }
    int countSubstrings(string s) 
    {
        int res = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            res += expend(s, i, i);
            res += expend(s, i, i + 1);

        }

        return res;
    }
};

int main()
{
    Solution sol;
    string str1 = "abc";
    string str2 = "aaa";
    int res1 = sol.countSubstrings(str1);
    int res2 = sol.countSubstrings(str2);
    cout << res1 << endl;
    cout <<res2 << endl;

}