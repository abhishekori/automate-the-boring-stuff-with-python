#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 00:01:56 2018

@author: abhishek
"""

def printPositions(positions):
    """To print the current postion
        @param postions list
        @return
    """

    for row in positions:
        for pos in row:
            print(str(pos),end='')
        print('\n')
    

def getInput():
    """
    reads input from command line
    @param
    @return string input from the commandline
    """
    n=input()
    return n

def checkRow(cur_player,row):
    """
    loops through the last input row and checks if 3 marks are there
    @param cur_player current player who played, row current row where the player               marks his positon

    """

    i=0
    for pos in range(3):
        if positions[row][pos]==cur_player:
            i+=1
    if i==3:
        return True
    else:
        return False
    
    
def checkColumn(cur_player,pos):
    """gets the current player and column. Loops through the column and checks if there are 3 marks"""
    i=0
    for row in range(3):
        if positions[row][pos]==cur_player:
            i+=1
    if i==3:
        return True
    else:
        return False
    

def checkDiagonal(cur_player,row,pos):
    """Checks the diagonals if there are 3 marks"""
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
    """this function will call checkColumn,checkRow and checkDiagonal and returns if any one of the checks returns true"""
    if checkRow(cur_player,row) == True or checkColumn(cur_player,pos)==True or checkDiagonal(cur_player,row,pos)==True:
        return True


positions=[[0,0,0],[0,0,0],[0,0,0]]
cur_player=1
pos=0    
printPositions(positions)


def startGame(positions,cur_player,pos):
    """This is the main program where it takes input, marks the users input on the board, checks each time of the entry and prints if someone has won or draw match"""
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

        cur_player=2 if cur_player==1 else 1
    print('Match draw')
       
"""Call the main program"""
startGame(positions,cur_player,pos)    

    
    
    
    




    


