# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:49:26 2024
@author: arshak
"""

import random
from PIL import Image

end = 100

def show_board():
    img = Image.open('slb.jpg')
    img.show()

def check_ladder(points):
    ladder_dict = {1: 38, 4: 14, 9: 31, 28: 84, 21: 42, 51: 67, 72: 91, 80: 99}
    if points in ladder_dict:
        print('Ladder!')
        return ladder_dict[points]
    return points

def check_snake(points):
    snake_dict = {17: 6, 54: 34, 62: 19, 64: 60, 87: 36, 93: 73, 95: 75, 98: 79}
    if points in snake_dict:
        print('Snake!')
        return snake_dict[points]
    return points

def reached_end(points):
    return points == end

def play():
    p1_name = input('Player 1, Please enter your name:')
    p2_name = input('Player 2, Please enter your name:')
    
    pp1 = 0 #points 
    pp2 = 0
    
    turn = 0
    
    while True:
        if turn % 2 == 0:
            print(p1_name,' Your Turn Bro')
            #ask players choice to continue
            c = int(input('Press 1 to continue or 0 to quit:'))
            if c == 0:
                print(p1_name,' scored ',pp1)
                print(p2_name,' scored ',pp2)
                print('Quitting the game, Thank you for playing!!')
                break
            dice = random.randint(1, 6)
            print('Dice rolled: ',dice)
            
            pp1 += dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            
            if pp1 > end: #if points exceeded 100
                pp1 = end
            print(p1_name,'Your current score: ',pp1)
            
            if reached_end(pp1):
                print(p1_name,'Won the game')
                break
        else:
            print(p2_name,' Your Turn Bro')
            #ask players choice to continue
            c = int(input('Press 1 to continue or 0 to quit:'))
            if c == 0:
                print(p1_name,' scored ',pp1)
                print(p2_name,' scored ',pp2)
                print('Quitting the game, Thank you for playing!!')
                break
            dice = random.randint(1, 6)
            print('Dice rolled: ',dice)
            
            pp2 += dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            
            if pp2 > end: #if points exceeded 100
                pp2 = end
            print(p2_name,'Your current score: ',pp2)
            
            if reached_end(pp2):
                print(p2_name,'Won the game')
                break
            
        turn += 1
    
show_board()
play()
