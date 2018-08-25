#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:15:00 2018

@author: abhishek
"""

import sys
import pyperclip
import random
from random import shuffle
import csv

if len(sys.argv)<2:
    print('Usage python password_gen.py [website name]')
    sys.exit()
    
website_name = sys.argv[1]
def appendToCsv(row):    
    with open('passwords.csv',mode='a') as pass_file:
        pass_writer=csv.writer(pass_file,delimiter=',')
        pass_writer.writerow(row)
   
    
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


with open('passwords.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        if row['website']==website_name:
            #print(f'{row["website"]} {row["password"]}')
            print(str(row['password']))
#            pyperclip.copy(str(row['password']))
#            #print(pyperclip.paste())
#            print(f'password for {row["website"]} copied to clipboard!')
            sys.exit()
    print(password)
    appendToCsv([website_name,password])
    print(f'New password generated for {website_name} and copied to clipboard!')
        
    
    

