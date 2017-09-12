#!/usr/bin/env python3
import random

def GuessNumber():
    ''' 猜数字游戏

    - 程序随机生成一个20以内的整数，用户有10次机会猜测
    - 程序根据用户输入，给予一定提示（大了、小了、正确）
    - 猜对或用完10次机会，游戏结束 '''
    answer = random.randint(0, 20)
    times = 10
    while times is not 0:
        try:
            number = int( input("请输入一个20以内的整数: ") )
        except:
            print("------这不是一个整数，请重新输入！")
            continue
        if not 0 <= number <= 20:
            print("------这不是20以内的整数，请重新输入！")
            continue
        else:
            times -=1
            if number > answer:
                print("------大了！可再猜{0}次！".format(times))
            elif number < answer:
                print("------小了！可再猜{0}次！".format(times))
            else:
                print("------正确，就是 {0!r} !".format(number))
                break
    else:
         print("10次未猜对，游戏终止！")

        
if __name__ == "__main__":
    GuessNumber()
            
