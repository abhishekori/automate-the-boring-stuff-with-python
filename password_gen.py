#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:15:00 2018

@author: abhishek
"""

import sys
import random
from random import shuffle

if len(sys.argv)<2:
    print('Usage python password_gen.py [account] [website]')
    sys.exit()
    
account_name = sys.argv[1]
website_name = sys.argv[2]

password=[]

for i in range(3):
    password.append(chr(random.randint(65,90)))

for i in range(7):
    password.append(chr(random.randint(97,122)))

for i in range(2):
    password.append(chr(random.randint(33,47)))
    
for i in range(2):
    password.append(str(random.randint(1,2)))
    
shuffle(password)
password="".join(password)

