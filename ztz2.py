# -*- coding: utf-8 -*-
"""
作者：kexinl
功能：模拟掷骰子
版本：2.0
日期：2019年1月2日
"""
import random

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    total_times = 100000
    
    
    result_list =[0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))
    
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        
        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1
    for i, result in roll_dict.items():
        print('点数{}的次数:{},频率:{}'.format(i, result, result / total_times))

if __name__ == '__main__':
    main()
