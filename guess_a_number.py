#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 23:22:46 2018

@author: abhishek
"""

import random
number=random.randint(1,20)
print('Guess a number. Clue? I think the number is inbetween 1-20')

input_ans=int(input())

while(input_ans!=number):
    if input_ans < number:
        print('your guess is too low')
    else:
        print('your guess is too high')
    print('take another guess!')
    input_ans=int(input())
    
print('Your guess it correct! the right answer is '+str(number))

