# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 16:24:50 2018

@author: Sasha
"""
"""
Imports stuff
"""
import pygame
#from pynput.mouse import Listener 
#import math
import random
#from pynput.mouse import Listener
"""
Intializes the game
"""
pygame.init()
"""
Returns the display board
"""
display_width = 1025
display_hight = 750
"""
Defines the colours
"""
white = (255 , 255 , 255)
grey = (125 , 125 , 125)
white = (255 , 255 , 255)
grey = (125 , 125 , 125)
"""
Shows which pictures go with which functions
"""
#Title_name = 'Title.jpg'
Win_name = 'BLUEWINS.jpg'
Lose_name = 'REDWINS.jpg'
image_name =  'yellow_rect.jpg'
RoyalGameofUr = "RoyalGameofUr.jpg"
image_name3 = "EXIT_GAME.jpg"
image_name4 = "Score.jpg"
RollDiceName = 'RollDice.jpg'
Dice0_name = "Dice0.jpg"
Dice1_name = "Dice1.jpg"
PlayerRed_name = 'PlayerRed.jpg'
PlayerBlue_name = 'PlayerBlue.jpg'
MakeATurn_name = 'MakeATurn.jpg'
ChipStorage_name = 'ChipStorage.jpg'
Score0_name = 'score0.jpg'
Score1_name = 'score1.jpg'
Score2_name = 'score2.jpg'
Score3_name = 'score3.jpg'
#image_name7 = "Dice2.jpg"
#image_name8 = "Dice3.jpg"
#image_name9 = "Dice4.jpg"
TokenBlue_name = 'Token_Blue.jpg'
TokenRed_name = 'Token_Red.jpg'
ExitGame = 'EXIT_GAME.jpg'
GameTurn = 0
Score = 0
# positions of blue chips - X,y, last is position on the board
# 0 not started , 1-12 - located on board , -1 - ended game 
BlueChips = [[20,200,0],[22,300,0],[20,400,0],[22,500,0]]
RedChips = [[400,200,0],[405,300,0],[400,400,0],[405,500,0]]
# Blue path coordinnates - third is a step number , forth shows if there is star
PathBlue = [[0,0,14,1], [0,0,13,0], [0,0,12,0],[0,0,11,0],[0,0,10,0],[0,0,9,0],[0,0,8,1],[0,0,7,0],[0,0,6,0],[0,0,5,0],[0,0,4,1],[0,0,3,0],[0,0,2,0],[0,0,1,0]]
# Same for Red -
PathRed = [[0,0,14,1], [0,0,13,0], [0,0,12,0],[0,0,11,0],[0,0,10,0],[0,0,9,0],[0,0,8,1],[0,0,7,0],[0,0,6,0],[0,0,5,0],[0,0,4,1],[0,0,3,0],[0,0,2,0],[0,0,1,0]]
RedBlueTurn = [0,0]
"""
Shows which pictures go with which functions
"""
#Title = pygame.image.load(Title_name)
Win = pygame.image.load(Win_name)
Lose = pygame.image.load(Lose_name)
Image1 = pygame.image.load(image_name)
RoyalGameofUr = pygame.image.load(RoyalGameofUr)
Image3 = pygame.image.load(image_name3)
Image4 = pygame.image.load(image_name4)
RollDice = pygame.image.load(RollDiceName)
PlayerRedImage =  pygame.image.load(PlayerRed_name)
PlayerBlueImage = pygame.image.load(PlayerBlue_name)
ImageDice0 = pygame.image.load(Dice0_name)
ImageDice1 = pygame.image.load(Dice1_name)
TokenBlue = pygame.image.load(TokenBlue_name)
TokenRed = pygame.image.load(TokenRed_name)
ExitGame = pygame.image.load(ExitGame)
MakeATurn =  pygame.image.load(MakeATurn_name)
ChipStorage = pygame.image.load(ChipStorage_name)
Score0 = pygame.image.load(Score0_name)
Score1 = pygame.image.load(Score1_name)
Score2 = pygame.image.load(Score2_name)
Score3 = pygame.image.load(Score3_name)

"""
Creates the Dicelist
"""
Dicelist = [0,0,0,0]
"""
Creates the Display
"""
gameDisplay = pygame.display.set_mode((display_width, display_hight))
pygame.display.set_caption('Game of Ur ')
crashed = False
def picture(Image, x,y):
    """
    Allows pictures to be shown
    """
    gameDisplay.blit((Image),(x,y))
    

#def exitGame():

#    if MOUSEBUTTONDOWN.picture(Image3, 530,10) == True:
#        pygame.quit()
def CheckIfBluePosition(position):
      ifFound = -1
      for i in range(4):
           if  BlueChips[i][2] == position:
               ifFound  = 1
               print('FoundBlue')
               return ifFound
           
def CheckIfRedPosition(position):
      ifFound = -1
      for i in range(4):
           if  RedChips[i][2] == position:
               ifFound  = 1
               print('FoundRed')
               return ifFound            
    
def CheckIfBlue(x,y,Score):
    PressedBlue = -1
    size = 92
    for i in range(4):
        if  BlueChips[i][0] <=x <=BlueChips[i][0]+size:
            if BlueChips[i][1]<=y<=BlueChips[i][1]+size:
                PressedBlue = i
                picture(MakeATurn, 530, 400)  
                picture(PlayerRedImage, 750, 300)
                if BlueChips[i][2] > -1:
                     NewPosition = BlueChips[i][2]+Score
                else:
                    NewPosition = 15     
                if  NewPosition <= 14:
                    BlueChips[i][2] = NewPosition
                else:
                    BlueChips[i][2] = -100
                print(NewPosition)
# add logic to move the seelcted chip  
                for j in range(14):
                  if PathBlue[j][2] == NewPosition:
# check if there is another same color chip on same place 
                      ifBlue = CheckIfBluePosition(NewPosition)
                      if ifBlue == 1:
# chnage the logic later                          
                        BlueChips[i][0] = PathBlue[j][0]+8
                        BlueChips[i][1] = PathBlue[j][1]+8    
                      else:
                        BlueChips[i][0] = PathBlue[j][0]+4
                        BlueChips[i][1] = PathBlue[j][1]+4  
                      ifRed = CheckIfRedPosition(NewPosition)
                      if ifRed == 1:
                        BlueChips[i][0] = PathBlue[j][0]+8
                        BlueChips[i][1] = PathBlue[j][1]+8 
                        if 4 < NewPosition < 12:
                            for k in range(4):
# move back yo the board                            
                              if RedChips[k][2]==NewPosition:
                                  RedChips[k][2]=0
                                  RedChips[k][0]=400
                                  RedChips[k][1]=200+k*100
                      
                
# display new chip positions
    Initialize_Board(110,10)                  
    DrawTokensBlue() 
    DrawTokensRed() 
#    picture(PlayerRedImage, 750, 300)
#    picture(MakeATurn, 530, 400)                   
    pygame.display.flip()
    print(PressedBlue)
    return PressedBlue

def CheckIfRed(x,y,Score):
    PressedRed = -1
    size = 92
    for i in range(4):
        if  RedChips[i][0] <=x <=RedChips[i][0]+size:
            if RedChips[i][1]<=y<=RedChips[i][1]+size:
                PressedRed = i
                picture(MakeATurn, 530, 400)
                picture(PlayerBlueImage, 750, 300)
                if BlueChips[i][2] > -1:
                     NewPosition = RedChips[i][2]+Score
                else:
                    NewPosition = 15
                print(NewPosition)
                if  NewPosition <= 14:
# check if it is not taken by same color chip - if yes move to the next field ?                    
                    RedChips[i][2] = NewPosition
# calculate new position of the chip                     
                else:
                    RedChips[i][2] = -100  # end of game for this chip
                for j in range(14):
                  if PathRed[j][2] == NewPosition:
# check if there is another same color chip on same place   
# check if opposite color on same place                      
                      RedChips[i][0] = PathRed[j][0]+4
                      RedChips[i][1] = PathRed[j][1]+4
                      if 4 < NewPosition < 12:
                            for k in range(4):
# move back yo the board                            
                              if BlueChips[k][2]==NewPosition:
                                  BlueChips[k][2]=0
                                  BlueChips[k][0]=20
                                  BlueChips[k][1]=200+k*100
# add logic to move the seelcted chip 
    Initialize_Board(110,10)                  
    DrawTokensRed() 
    DrawTokensBlue()                    
#   picture(PlayerBlueImage, 750, 300)
#    picture(MakeATurn, 530, 400)
    pygame.display.flip()
    print(PressedRed)
    return PressedRed

        
def mouseControl(x,y):
    """
    Controls the mouse
    """
    global GameTurn
#    print(x,y)
    global  Score 
    BlueNumber = 0
    PlayerTurn = GameTurn%2
    if RedBlueTurn[0]:
        BlueNumber = CheckIfBlue(x,y,Score)
        if BlueNumber >= 0:
            RedBlueTurn[0]=0 # free for red turn
            Score = 0 # reset score
    if RedBlueTurn[1]:
        RedNumber = CheckIfRed(x,y,Score) 
        if RedNumber >= 0:
            RedBlueTurn[1] = 0 #free for blue turn
            Score = 0 # reset score
    if 800 >= x_pos >= 530:
        if 10 <= y_pos <= 100:
# pressed on exit Game rectangle            
            pygame.quit()
    if 910 >= x_pos >= 530:
        if 275 <= y_pos <= 366:
# pressed on Cast Dice Button   
# works only if both turns and zeros otherwise wait for the move 
            if  RedBlueTurn[0] +  RedBlueTurn[1] == 0:
                print(RedBlueTurn[0] ,  RedBlueTurn[1])
                Score = 0
                for i in range(4):
                    Dicelist[i] = random.randint(0,1)
                    if Dicelist[i] == 0:
                        picture(ImageDice0, 530+i*98, 400)
                    else:
                        picture(ImageDice1, 530+i*98, 400)
                        Score = Score + 1
                
                if PlayerTurn == 1:#red player
                    picture(PlayerRedImage, 750, 300)
                    RedBlueTurn[1] = 1
                    RedBlueTurn[0] = 0
                    GameTurn = GameTurn + 1
                else:
                    picture(PlayerBlueImage, 750, 300)
                    RedBlueTurn[1] = 0
                    RedBlueTurn[0] = 1
                    GameTurn = GameTurn + 1
            pygame.display.flip()
#            GameTurn = GameTurn + 1
            PlayerTurn = GameTurn%2
            print(GameTurn)
#                drawDice(Dicelist[])
 
def Initialize_Board(x,y):
#    
#    """
#    Returns a Picture of the Gameboard and all of the buttons
#    """
#     gameDisplay.fill(grey)
     size = 92
     # first row
     PathBlue[0][0]=x
     PathBlue[0][1]=y+size
     PathRed[0][0]=x+2*size
     PathRed[0][1]=y+size
     
     PathBlue[1][0]=x
     PathBlue[1][1]=y
     PathRed[1][0]=x+2*size
     PathRed[1][1]=y
     
     PathBlue[2][0]=x+size
     PathBlue[2][1]=y
     PathRed[2][0]=x+size
     PathRed[2][1]=y
     
     PathBlue[3][0]=x+size
     PathBlue[3][1]=y+size
     PathRed[3][0]=x+size
     PathRed[3][1]=y+size
     
     PathBlue[4][0]=x+size
     PathBlue[4][1]=y+2*size
     PathRed[4][0]=x+size
     PathRed[4][1]=y+2*size
     
     PathBlue[5][0]=x+size
     PathBlue[5][1]=y+3*size
     PathRed[5][0]=x+size
     PathRed[5][1]=y+3*size
     
     PathBlue[6][0]=x+size
     PathBlue[6][1]=y+4*size
     PathRed[6][0]=x+size
     PathRed[6][1]=y+4*size
     
     PathBlue[7][0]=x+size
     PathBlue[7][1]=y+5*size
     PathRed[7][0]=x+size
     PathRed[7][1]=y+5*size
     
     PathBlue[8][0]=x+size
     PathBlue[8][1]=y+6*size
     PathRed[8][0]=x+size
     PathRed[8][1]=y+6*size
    
     PathBlue[9][0]=x+size
     PathBlue[9][1]=y+7*size
     PathRed[9][0]=x+size
     PathRed[9][1]=y+7*size
    
     PathBlue[10][0]=x
     PathBlue[10][1]=y+7*size
     PathRed[10][0]=x+2*size
     PathRed[10][1]=y+7*size
    
     PathBlue[11][0]=x
     PathBlue[11][1]=y+6*size
     PathRed[11][0]=x+2*size
     PathRed[11][1]=y+6*size
     
     PathBlue[12][0]=x
     PathBlue[12][1]=y+5*size
     PathRed[12][0]=x+2*size
     PathRed[12][1]=y+5*size
     
     PathBlue[13][0]=x
     PathBlue[13][1]=y+4*size
     PathRed[13][0]=x+2*size
     PathRed[13][1]=y+4*size
     
     for i in range(14):
        picture(Image1, PathBlue[i][0],PathBlue[i][1]) 
        picture(Image1, PathRed[i][0],PathRed[i][1]) 
        if PathBlue[i][3] == 1:
# means that it is a star field            
                    picture(RoyalGameofUr, PathBlue[i][0]+5,PathBlue[i][1]+5)
        if PathRed[i][3] == 1:
# means that it is a star field             
                    picture(RoyalGameofUr, PathRed[i][0]+5,PathRed[i][1]+5)            

     
#     picture(ExitGame, 530,10)
#     picture(Image4, 530, 100)
#     picture(RollDice, 530, 275)
     pygame.display.flip()

def Intitialize_Score():
     picture(ExitGame, 530,10)
     picture(Image4, 530, 100)
     picture(RollDice, 530, 275)
     pygame.display.flip()

def Tokens(Dice_Image,x,y):
    """
    Returns a Picture of the Tokens
    """
    size = 92
    picture(Dice_Image, x,y)
    pygame.display.flip()
     
def DrawTokensBlue():
    picture(ChipStorage, 10,182)
    BlueScore = 0
    picture(Score0, 650, 185)
    for i in range(4):
        if BlueChips[i][2] > -10:
# - 1 means that the chip reached the end of game                
            Tokens(TokenBlue,BlueChips[i][0],BlueChips[i][1])
        else:
            BlueScore = BlueScore + 1
        if BlueScore == 1:
            picture(Score1, 650, 185)
        elif BlueScore == 2:
            picture(Score2, 900, 185)
        elif BlueScore == 3:
            picture(Score3, 900, 185)
        elif BlueScore == 4:
            picture(Win, 0, 0) 
# add logic to show correct count             
    
           
        
        
def DrawTokensRed():
    picture(ChipStorage, 390,182)
    RedScore = 0 
    picture(Score0, 900, 185)  
    for i in range(4):
        if RedChips[i][2] > -10:
# - 1 means that the chip reached the end of game            
            Tokens(TokenRed,RedChips[i][0],RedChips[i][1]) 
        else:
            RedScore = RedScore + 1
        if RedScore == 1:
            picture(Score1, 900, 185)
        elif RedScore == 2:
            picture(Score2, 900, 185)
        elif RedScore == 3:
            picture(Score3, 900, 185)
        elif RedScore == 4:
            picture(Lose, 0, 0)    
# add logic to show correct count             
           
    
#picture(ExitGame, 450,450)
gameDisplay.fill(grey)        
Initialize_Board(110,10)
Intitialize_Score()
DrawTokensBlue()
DrawTokensRed()



#def drawDice(Dicelist):

#    for i in range(4):
#        if DiceList[i] == 1:
#            DiceList[i] = 1
#            picture(image_Dice1, 700, 700)
#        else :
#            DiceList[i] = 0
#            picture(image_Dice0, 700, 700)
        
    

def Mouse_Pressed(x,y):
    """
    Checks if the Mouse is pressed
    """
    print('clicked on image', x , y)
    
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
          
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = event.pos
            mouseControl(x_pos,y_pos)
            
#            crashed = True
       
        
pygame.quit()
          
quit()
       