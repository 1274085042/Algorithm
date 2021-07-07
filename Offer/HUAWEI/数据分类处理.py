#coding=utf-8

'''
题目描述
信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、 QQ 用户、手机号码、银行帐号等信息及活动记录。
采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。

输入描述:
﻿一组输入整数序列I和一组规则整数序列R，I和R序列的第一个整数为序列的个数（个数不包含第一个整数）；整数范围为0~0xFFFFFFFF，序列个数不限

输出描述:
﻿从R依次中取出R<i>，对I进行处理，找到满足条件的I<j>：

I<j>整数对应的数字需要连续包含R<i>对应的数字。比如R<i>为23，I<j>为231，那么I<j>包含了R<i>，条件满足 。

按R<i>从小到大的顺序:

(1)先输出R<i>；

(2)再输出满足条件的I<j>的个数；

(3)然后输出满足条件的I<j>在I序列中的位置索引(从0开始)；

(4)最后再输出I<j>。

附加条件：

(1)R<i>需要从小到大排序。相同的R<i>只需要输出索引小的以及满足条件的I<j>，索引大的需要过滤掉

(2)如果没有满足条件的I<j>，对应的R<i>不用输出

(3)最后需要在输出序列的第一个整数位置记录后续整数序列的个数(不包含“个数”本身)

序列I：15,123,456,786,453,46,7,5,3,665,453456,745,456,786,453,123（第一个15表明后续有15个整数）

序列R：5,6,3,6,3,0（第一个5表明后续有5个整数）

输出：30, 3,6,0,123,3,453,7,3,9,453456,13,453,14,123,6,7,1,456,2,786,4,46,8,665,9,453456,11,456,12,786

说明：

30----后续有30个整数

3----从小到大排序，第一个R<i>为0，但没有满足条件的I<j>，不输出0，而下一个R<i>是3

6--- 存在6个包含3的I<j>

0--- 123所在的原序号为0

123--- 123包含3，满足条件 题目描述
信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、 QQ 用户、手机号码、银行帐号等信息及活动记录。

采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。

﻿
输入描述:
﻿一组输入整数序列I和一组规则整数序列R，I和R序列的第一个整数为序列的个数（个数不包含第一个整数）；整数范围为0~0xFFFFFFFF，序列个数不限

输出描述:
﻿从R依次中取出R<i>，对I进行处理，找到满足条件的I<j>：

I<j>整数对应的数字需要连续包含R<i>对应的数字。比如R<i>为23，I<j>为231，那么I<j>包含了R<i>，条件满足 。

按R<i>从小到大的顺序:

(1)先输出R<i>；

(2)再输出满足条件的I<j>的个数；

(3)然后输出满足条件的I<j>在I序列中的位置索引(从0开始)；

(4)最后再输出I<j>。

附加条件：

(1)R<i>需要从小到大排序。相同的R<i>只需要输出索引小的以及满足条件的I<j>，索引大的需要过滤掉

(2)如果没有满足条件的I<j>，对应的R<i>不用输出

(3)最后需要在输出序列的第一个整数位置记录后续整数序列的个数(不包含“个数”本身)


序列I：15,123,456,786,453,46,7,5,3,665,453456,745,456,786,453,123（第一个15表明后续有15个整数）

序列R：5,6,3,6,3,0（第一个5表明后续有5个整数）

输出：30, 3,6,0,123,3,453,7,3,9,453456,13,453,14,123,6,7,1,456,2,786,4,46,8,665,9,453456,11,456,12,786

说明：

30----后续有30个整数

3----从小到大排序，第一个R<i>为0，但没有满足条件的I<j>，不输出0，而下一个R<i>是3

6--- 存在6个包含3的I<j>

0--- 123所在的原序号为0

123--- 123包含3，满足条件
'''
def quchong_pailie(l):
    s=list(set(l))
    s.sort()
    return s

def fuheguize(input_l,regulation_l):
    record_dic={}

    for i in regulation_l:
        index_value = []
        count = 0
        for j in range(len(input_l)):

            if str(i) in str(input_l[j]):
                count+=1
                index_value.append(j)
                index_value.append(input_l[j])
        index_value.insert(0,count)
        record_dic[i]=index_value

    return record_dic
def outp(regulationl,rc):
    count=0
    res=[]
    for i in regulation_l:
        if rc[i][0]!=0:
            count=len(rc[i])+1+count
    res.append(count)
    for i  in regulation_l:
        if rc[i][0]!=0:
            res.append(i)
            res.extend(rc[i])
    return res

while True:
    try:
        input_seq=list(map(int,input().strip().split(' ')))
        # input_seq=[15,123,456,786,453,46,7,5,3,665,453456,745,456,786,453,123]
        # regulation_seq=[5,6,3,6,3,0]
        regulation_seq=list(map(int,input().strip().split(' ')))
        input_num=input_seq[0]
        regulation_num=regulation_seq[0]
        input_list=input_seq[1:]
        regulation_list=regulation_seq[1:]
        regulation_l=quchong_pailie(regulation_list)
        rc=fuheguize(input_list,regulation_l)
        #print(rc)
        res=list(map(str,(outp(regulation_l,rc))))
        result=" ".join(res)

        print(result)
    except:
        break
