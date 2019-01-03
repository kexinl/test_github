# -*- coding: utf-8 -*-
"""
作者：kexinl
功能：模拟掷骰子
版本：3.0
日期：2019年1月3日
"""
import random
import matplotlib.pyplot as plt

def roll_dice():
    roll = random.randint(1, 6)
    return roll

def main():
    total_times = 100
    
    result_list =[0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))
    
    roll1_list = []
    roll2_list = []
    
    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        
        roll1_list.append(roll1)
        roll2_list.append(roll2)
        
        for j in range(2, 13):
            if (roll1 + roll2) == j:
                roll_dict[j] += 1
    for i, result in roll_dict.items():
        print('点数{}的次数:{},频率:{}'.format(i, result, result / total_times))
    
    x = range(1, total_times + 1)
    plt.scatter(x, roll1_list, c = 'red', alpha = 0.5)
    plt.scatter(x, roll2_list, c= 'black', alpha = 0.5)
    plt.show()
    
if __name__ == '__main__':
    main()
