#coding=utf-8

'''
题目描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

接口说明

/**
 * 反转句子
 *
 * @param sentence 原句子
 * @return 反转后的句子
 */
public String reverse(String sentence);

输入描述:
将一个英文语句以单词为单位逆序排放。

输出描述:
得到逆序的句子
'''

def sentence_reverse(sen):
    sen_list=sen.split(" ")
    sen_list=reversed(sen_list)
    sen_reverse=" ".join(sen_list)
    return sen_reverse

sen=input()
print(sentence_reverse(sen))
