#coding=utf-8
# I am not responsible of this code.
# They made me write it, against my will.
'''
题目描述
问题描述：数独（Sudoku）是一款大众喜爱的数字逻辑游戏。玩家需要根据9X9盘面上的已知数字，
推算出所有剩余空格的数字，并且满足每一行、每一列、每一个粗线宫内的数字均含1-9，并且不重复。
输入：
包含已知数字的9X9盘面数组[空缺位以数字0表示]
输出：
完整的9X9盘面数组

输入描述:
包含已知数字的9X9盘面数组[空缺位以数字0表示]

输出描述:
完整的9X9盘面数组
'''

class SudoSolution():
    def __init__(self,board):
        self.board=board
        self.dict=['1','2','3','4','5','6','7','8','9']


    def search_position(self):
        '''
         查找空格子的位置，如果没有空格子，说明已经填好
         '''
        for i in range(9):
            for j in range(9):
                if self.board[i][j]=='0':
                    return i,j
        return -1,-1


    def Slove(self):
        '''
        递归函数
        '''
        row,column=self.search_position()
        if row==-1 and column==-1:          #递归终止条件，没有找到空格子
            return True
        else:
            for num in self.dict:
                if self.check(num,row,column):         #检查填入的数字是否符合要求
                    self.board[row][column]=num
                    '''
                    如果填入的数字符合要求，
                    递归，查找下一个空格子
                    '''
                    if self.Slove():
                        return  True
                    else:                   #回溯:要填入的数字使下一次递归不成功，因此将当前网格重置为‘0’
                        self.board[row][column] = '0'

            return False                    #所有的数字试完之后都没有符合要求的


    def check(self,num,row,column):
        return self.check_row(num,row) and self.check_column(num,column) and self.check_box(num,row,column)

    def check_row(self,num,row):
        for j in range(9):
            if self.board[row][j]==num:
                return False

        return True

    def check_column(self,num,column):
        for i in range(9):
            if self.board[i][column]==num:
                return False

        return True

    def check_box(self,num,row,column):
        box_row=row-row%3               #3*3左上角网格的行下标
        box_column=column-column%3      #3*3左上角网格的列下标

        for i in range(box_row,box_row+3):
            for j in range(box_column,box_column+3):
                if self.board[i][j]==num:
                    return False
        return True



# board = [
#     ['5', '3', '0', '0', '7', '0', '0', '0', '0'],
#     ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
#     ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
#     ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
#     ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
#     ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
#     ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
#     ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
#     ['0', '0', '0', '0', '8', '0', '0', '7', '9']]
# solution=SudoSolution(board)
# #print(solution.board)
# if solution.Slove():
#     for v in solution.board:
#         print(" ".join(v))

while True:
    try:
        board=[input().strip().split() for i in range(9)]
        solution=SudoSolution(board)
        #print(solution.board)
        if solution.Slove():
            for v in solution.board:
                print(" ".join(v))
    except:
        break
