/*
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int MoreThanHalfNum(vector<int> &numbers)
    {
        int length=numbers.size();
        int num=numbers[0];     //找出出现频率最高数
        int times=1;

        for(int i=1;i<length;i++)
        {
            if(times==0)
            {
                num=numbers[i];
                times=1;
            }
            else
            {
                   if(num!=numbers[i])
            {
                times--;
            }
            else
            {
                times++;
            }


            }
         
        }

        if(times>0)
        {
            return num;
        }
        else
        {
            return 0;
        }
        
    }

    bool CheckMoreHalf(vector<int> &numbers,int num)
    {
        int times=0;
        int len=numbers.size();
        for(int i=0;i<len;i++)
        {
            if(num==numbers[i])
            {
                times++;
            }
        }
        if(2*times>len)
        {
            return true;
        }
        else
        {
            return false;
        }
        

    }

    int MoreThanHalfNum_Solution(vector<int> numbers)
    {
    if (numbers.size()==0)
    {
        return 0;
    }
     int num=MoreThanHalfNum(numbers);
    if(CheckMoreHalf(numbers,num))
    {
        return num;
    }
    else
    {
        return 0;
    }
        
    }

    //int  Check
};


int main()
{
vector<int> numbers={1,2,3,2,2};
Solution s;
int num=s.MoreThanHalfNum_Solution(numbers);
cout<<num<<endl;

return 0;
}