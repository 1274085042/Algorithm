#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
有一只兔子，从出生后第3个月起每个月都生一只兔子，
小兔子长到第三个月后每个月又生一只兔子，假如兔子都不死，
问每个月的兔子总数为多少？
    /**
     * 统计出兔子总数。
     *
     * @param monthCount 第几个月
     * @return 兔子总数
     */
    public static int getTotalCount(int monthCount)
    {
        return 0;
    }
输入描述:
输入int型表示month

输出描述:
输出兔子总数int型
'''

def f(n):
    if n<3:
        return 1
    #该月兔子的数量=上个月兔子的数量+这个月新生的兔子（两个月前兔子的数量）
    else:
        return f(n-1)+f(n-2)
#print(f(9))
while True:
    try:
        n=int(input().strip())
        print(f(n))
    except:
        break