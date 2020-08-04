from bCube import *
from bBoard import *
from bGame import *
from random import *
from math import *
import time

class bGame:

    #__init__: boggleBoard, string -> void
    def __init__(self,bBoard,scoreFile):

        # instance variables

        self.bBoard = bBoard        # boggle board
        self.scoreFile = scoreFile  # name of file for scoring

    # accessor methods

    # getBoard: -> boggle Board
    def getBoard(self):
        return self.bBoard

    # getFile: -> string
    def getFile(self):
        return self.scoreFile
    
    # mutator methods

    # setBoardSize: bBoard -> void
    def setBoard(self,newBoard):
        self.bBoard = newBoard

    # setFile: string -> void
    def setFile(self,newFile):
        self.scoreFile = newFile
        
    # special methods

    # gameTimer: int -> void
    def gameTimer(self,t):
        # t is time in seconds
        # prints time remaining every 30 seconds
        while t:
            mins, secs = divmod(t, 60)
            timeRemaining = '{:02d}:{:02d}'.format(mins, secs)
            print(timeRemaining)
            time.sleep(30)
            t -= 30
        print('Game over!\nPlease enter your score.')

    # play: int -> void
    def play(self,gameTime):
        self.bBoard.shake()
        print(self.bBoard)
        self.gameTimer(gameTime)

    # score: -> [score, string]
    def score(self):
        # read and pre-process word list
        bWordFile = open(self.scoreFile)
        bWordList = bWordFile.readlines()
        bWordList = [word.strip('\n') for word in bWordList]
    
        totalScore = 0
        longestWord=""
        
        for word in bWordList:
            wordlength = len(word)
            if wordlength < 3:
                wordScore = 0
            if wordlength == 3 or wordlength == 4:
                wordScore = 1
            elif wordlength == 5:
                wordScore = 2
            elif wordlength == 6:
                wordScore = 3
            elif wordlength == 7:
                wordScore = 5
            else:
                wordScore = 11

            if wordlength > len(longestWord):
                    longestWord = word
            totalScore = totalScore + wordScore
        return [totalScore,longestWord]

    # __str__: -> string
    def __str__(self):
        scoreInfo = self.score()
        scoreString = "Your score was " + str(scoreInfo[0]) + "\n"
        bestWordString = "Your longest word was " + scoreInfo[1]
        return str(self.bBoard) + '\n\n' + scoreString + bestWordString
        
        
