from bCube import *
from random import *
from math import *

class bBoard:

    # __init__: list of bCubes -> void
    def __init__(self,aCubeList):

        # instance variables

        self.cubeList = aCubeList        # list of bCubes
        self.boardSize = len(aCubeList)  # number of holes in board
        self.board = [str(cube) for cube in self.cubeList]  # list of facing characters


    # accessor methods

    # getCubeList: -> list of bCubes
    def getCubeList(self):
        return self.cubeList

    # getBoardSize: -> integer
    def getBoardSize(self):
        return self.boardSize

    # getBoard: -> list of strings
    def getBoard(self):
        return self.board

    # mutator methods

    # setCubeList: list of bCubes -> void
    def setCubeList(self,aCubeList):
        self.cubeList = aCubeList
        self.boardSize = len(aCubeList)

    # setBoardSize: integer -> void
    def setBoardSize(self,n):
        self.BoardSize = n

    # setBoard: list of strings -> void
    def setBoard(self,newBoard):
        self.board = newBoard

    # special methods

    # insert the use of this method later to check for square
    # isSquare: -> boolean
    def isSquare(self):
        return sqrt(self.boardSize) == int(sqrt(self.boardSize))

    
    # shake: -> void
    def shake(self):

        shuffle(self.cubeList)                                 # shuffle cubes
        [cube.roll() for cube in self.cubeList]                # roll each cube
        self.board = [str(cube) for cube in self.cubeList]     # convert to list of strings        

    # currently assumes square board
    #__str__: -> string
    def __str__(self):
        rowLetters = [] # list of strings. one for each row
        sideLength = int(sqrt(self.boardSize))
        for i in range(sideLength):
            rowLetters.append(str(self.board[sideLength*i]))
            for j in range(1,sideLength):
                rowLetters[i] = rowLetters[i]+'    ' + str(self.board[sideLength*i+j])

        boardString = ''
        for i in range(sideLength):
            boardString = boardString + rowLetters[i] + '\n'

        return boardString
        
        
            
        
