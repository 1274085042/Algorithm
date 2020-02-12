#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

处理：
1、 记录最多8条错误记录，循环记录，(列表记录)
对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；（字典统计）
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
3、 输入的文件可能带路径，记录文件名称不能带路径。
输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。
输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开
'''

file_name_num_err={}
file_name_num_list=[]

while True:
    try:
        #input=r'E:\V1R2\product\fpgadrive.c 1325'
        file_path,line_num=input().strip().split(' ')
        if file_path=='':
             break
        file_path_list=file_path.split('\\')
        # print(file_path_list)
        file_name=file_path_list[-1]
        #print(file_name)
        if len(file_name)>16:
            file_name=file_name[-16:]
        file_name_num=file_name+' '+line_num
        if file_name_num not in file_name_num_err:
            file_name_num_list.append(file_name_num)
            file_name_num_err[file_name_num]=1
        else:
            file_name_num_err[file_name_num] += 1

    except:
        break


for i in file_name_num_list[-8:]:
    print(i+' '+str(file_name_num_err[i]))

