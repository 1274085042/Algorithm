#include <iostream>
#include <string>

using namespace std;

void Permutation(string );
void Permutation(string str, int begin);  //str代表整个字符串，begin：待排列字符串中第一个字符的下标

int main()
{
	//char *s = "abc";
	string s = "abcd";
	//cout<<s<<endl;
	Permutation(s);
	system("pause");
	return 0;
}

void Permutation(string str)
{
	if (str.size() == 0)
		return;
	else
		Permutation(str, 0);
}

void Permutation(string str, int  begin)
{
	if (str[begin] == '\0')
	{
		cout << str << endl;
	}
	for (int c = begin; str[c] != '\0'; c++)   //c：待交换字符的下标
	{
		char temp = str[c];
		str[c] = str[begin];
		str[begin] = temp;
		Permutation(str, begin + 1);
	}

}
