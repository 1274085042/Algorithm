#coding=utf-8

'''
题目描述
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
    /**
     * 统计出第5次落地时，共经过多少米?
     *
     * @param high 球的起始高度
     * @return 英文字母的个数
     */
    public static double getJourney(int high)
    {
        return 0;
    }

    /**
     * 统计出第5次反弹多高?
     *
     * @param high 球的起始高度
     * @return 空格的个数
     */
    public static double getTenthHigh(int high)
    {
        return 0;
    }

输入描述:
输入起始高度，int型

输出描述:
分别输出第5次落地时，共经过多少米第5次反弹多高
'''
def solution(high):

    to=high
    for i in range(4):
        to+=high
        high=high/2
    return  to,high/2

while True:
    try:
        high=int(input().strip())
        to,h=solution(high)
        print(round(to))
        print(round(h,2))
    except:
        break
