#coding=utf-8

'''
题目描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
    /**
     * 统计出英文字母字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getEnglishCharCount(String str)
    {
        return 0;
    }

    /**
     * 统计出空格字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 空格的个数
     */
    public static int getBlankCharCount(String str)
    {
        return 0;
    }

    /**
     * 统计出数字字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getNumberCharCount(String str)
    {
        return 0;
    }

    /**
     * 统计出其它字符的个数。
     *
     * @param str 需要输入的字符串
     * @return 英文字母的个数
     */
    public static int getOtherCharCount(String str)
    {
        return 0;
    }

'''

def statistic(str):
    Englishchar=0
    Blankchar=0
    Numberchar=0
    Otherchar=0
    for i in range(len(str)):
        if 'a'<=str[i]<='z' or 'A'<=str[i]<='Z':
            Englishchar+=1
        elif str[i]==' ':
            Blankchar+=1
        elif '0'<=str[i]<='9':
            Numberchar+=1
        else:
            Otherchar+=1

    return Englishchar,Blankchar,Numberchar,Otherchar
while True:
    try:

#str=r"1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\]["
#str=repr(input())
#str=str[1:-1]
        str=input()
        #print(str)

        Englishchar,Blankchar,Numberchar,Otherchar=statistic(str)
        print(Englishchar)
        print(Blankchar)
        print(Numberchar)
        print(Otherchar)
    except:
        break
