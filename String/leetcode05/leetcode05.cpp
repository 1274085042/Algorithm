#include <string>
#include <iostream>

using namespace std;

class Solution 
{
public:
    string replaceSpace(string s) 
    {
        int oldSize = s.size();
        int count = 0;
        for (int i = 0; i < oldSize; ++i)
        {
            if (s[i] == ' ')
            {
                ++count;
            }
        }
        s.resize(oldSize + count * 2);
        int newSize = s.size();
        int i = newSize-1;
        int j = oldSize-1;
        for (i, j; i != j; --i, --j)
        {
            if (s[j] != ' ')
            {
                s[i] = s[j];
            }
            else
            {
                s[i] = '0';
                s[i - 1] = '2';
                s[i - 2] = '%';
                i -= 2;
            }
        }

        return s;
    }
};

int main()
{
    string str = "We are happy";
    Solution sol;
    str = sol.replaceSpace(str);
    cout << str << endl;
}