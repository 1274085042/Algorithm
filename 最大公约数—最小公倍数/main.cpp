#include <iostream>
using namespace std;

int Max_yueshu(int ,int );
int main()
{
    int a,b;
    cout<<"Please input two number:";
    cin>>a>>b;
    cout<<"Max common divisor: "<<Max_yueshu(a,b)<<endl;
    //两个数的最小公倍数为(a*b)/最大公倍数
    cout<<"Min common multipul: "<<(a*b)/Max_yueshu(a,b)<<endl;
    system("pause");
    return 0;

}

/*
辗转相除法求最大公约数，
c=a%b（a一定要大于b）如果余数c是0，则b是最大公约数，否则，
a=b,b=c,一直循环，知道c为0，则b就是最大公约数。
*/
int Max_yueshu(int a,int b)
{
    int temp;
    if (a<b)
    {
        int c;
        c=a;
        a=b;
        b=c;
    }

    while(a%b!=0)
    {
        temp=a%b;
        a=b;
        b=temp;

    }
    return b;

}