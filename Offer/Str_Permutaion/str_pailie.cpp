/*
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba
*/
#include <iostream>
#include <string>
#include <vector>
#include <iterator>
#include <set>

using namespace std;
/*
void Permutation(string ,vector<string> *);
void Permutation(string str, int begin,vector<string> *);  //str代表整个字符串，begin：待排列字符串中第一个字符的下标 

int main()
{
	vector<string> res;
	//char *s = "abc";
	string s = "abc";
	//cout<<s<<endl;
	Permutation(s,&res);
	vector<string> :: iterator p;
	for(p=res.begin();p!=res.end();p++)
		cout<<*p<<endl;
	system("pause");

	return 0;
}

void Permutation(string str,vector<string> *res)
{
	if (str.size() == 0)
		return;
	else
		Permutation(str, 0,res);
}

void Permutation(string str, int  begin,vector <string> *res)  //待排序字符串的第一个字符下标索引
{
	if (str[begin] == '\0')
	{
		(*res).push_back(str);
		//cout << str << endl;
	}
	for (int c = begin; str[c] != '\0'; c++)   //c：待交换字符的下标
	{
		char temp = str[c];
		str[c] = str[begin];
		str[begin] = temp;
		Permutation(str, begin + 1,res);
	}

}
*/
class Solution {
    
public:
    vector<string> Permutation(string str) 
	{
		set<string> r;
        vector<string> res;
        if (str.size()==0)
            return res;
        else 
            permutation(str,0,&r);
			for(auto p=r.begin();p!=r.end();p++)
			{
				res.push_back(*p);
			}
            return res;
    }
    void permutation(string str,int begin,set <string> *r)
    {
        if(str[begin]=='\0')
            (*r).insert(str);
        for(int c=begin;str[c]!='\0';c++)
        {
            char temp=str[begin];
            str[begin]=str[c];
            str[c]=temp;
            permutation(str,begin+1,r);
            
        }
    }
};


int main()
{
	//ostream_iterator<string,char> out(cout," ");
	//string s1[4]={"bac","cab","abc"};

	//set<string> se(s1,s1+4);
	//copy(se.begin(),se.end(),out);

	string str="aa";
	Solution S;
	vector<string> res=S.Permutation(str);
	for(auto p=res.begin();p!=res.end();p++)
	{
		cout<<*p<<endl;
	}
	system("pause");
	return 0;

}