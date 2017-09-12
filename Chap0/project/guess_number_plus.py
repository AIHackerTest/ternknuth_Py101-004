#!/usr/bin/env python3
import random

def GuessNumberPlus():
    ''' 猜数字游戏（升级版）

    - 程序内部用0-9生成一个4位数，每个数位上的数字不重复，且首位数字不为零。
    - 用户输入4位数进制猜测，程序返回相应提示：
        + 用A表示数字和位置都正确，用B表示数字正确但位置错误
        + 用户猜测后，程序返回A和B的数量（如：2A1B）
    - 猜对或用完10次机会，游戏结束。  '''
    guess_num_list = [0, 0, 0, 0]
    while guess_num_list[0] == 0:
        num_list = list( range(0,10) )
        guess_num_list = random.sample(num_list, 4)
    else:
        #print(guess_num_list)   # observer
        pass

        
    times = 10
    while times:
        A = 0  # 
        B = 0  # 
        answer = input("请输入一个4位数： ")
        if len(answer) != 4 or ( not answer.isdigit() ):
            print("---------这不是一个4位数，请重新输入。")
            continue
        else:
            pass
        
        for i in range(0, 4):
            if int(answer[i]) in guess_num_list: 
                B += 1
                if int(answer[i]) == guess_num_list[i]:
                    A += 1
                    B -= 1
                else:
                    pass
            else:
                pass
        else:
            times -= 1
            if A == 4:
                print( "猜对了，{0!r}是正确答案!".format(answer) )
                exit(0)
            else:
                print( "---------未猜对（提示：'{0}A{1}B'），可再猜{2}次！" .format(A, B, times) )
    else:
        print("10次未猜对，游戏终止！")
                
if __name__ == '__main__':
    GuessNumberPlus()
