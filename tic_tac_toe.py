#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 00:01:56 2018

@author: abhishek
"""
print('_|_|_')
print('_|_|_')
print('_|_|_')
def printPositions(positions):
    for row in positions:
        for pos in row:
            print(str(pos),end='')
        print('\n')
    
def getInput():
    n=input()
    return n

def checkGameStatus(positions):
    i=0
    for row in positions:
        for pos in row:
            if pos !=0:
                i=i+1
        if i==3:
            print(str(row))
                
        
def checkRow(cur_player,row):
    i=0
    for pos in range(3):
        if positions[row][pos]==cur_player:
            i+=1
    if i==3:
        return True
    else:
        return False
def checkColumn(cur_player,pos):
    i=0
    for row in range(3):
        if positions[row][pos]==cur_player:
            i+=1
    if i==3:
        return True
    else:
        return False
    

def checkDiagonal(cur_player,row,pos):
    c1=0
    c2=0
    j=2
    if (row==pos) or (row==0 and pos==2) or (row==2 and pos==0):
        for i in range(3):
            if positions[i][i]==cur_player:
                c1+=1
            if positions[i][j]==cur_player:
                c2+=1
            j-=1
        if c1==3 or c2==3:
            return True
    
    return False
        
    
    
    
def checkGame(cur_player,row,pos):
    if checkRow(cur_player,row) == True or checkColumn(cur_player,pos)==True or checkDiagonal(cur_player,row,pos)==True:
        return True


positions=[[0,0,0],[0,0,0],[0,0,0]]
cur_player=1
pos=0    
printPositions(positions)


def startGame(positions,cur_player,pos):
    for i in range(8):
        print(str(cur_player)+' Turn \n')
        input_pos=int(getInput())
        index=0
        for row in range(len(positions)):
            for pos in range(len(positions[row])):
                #print(str(row)+' '+str(pos))
                index+=1
                if index==input_pos and positions[row][pos]==0:
                    positions[row][pos]=cur_player
                    printPositions(positions)
                    if checkGame(cur_player,row,pos)==True:
                        print('Player '+str(cur_player)+' is the winner')
                        return True
                    
                    
                
    #    positions[pos]=cur_player
        cur_player=2 if cur_player==1 else 1
        #printPositions(positions)
    print('Match draw')
       

startGame(positions,cur_player,pos)    

    
    
    
    




    


