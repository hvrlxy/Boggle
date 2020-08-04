from random import *

class bCube:

    # __init__: list of strings -> void

    def __init__(self, aLetterList):

        # instance variables

        self.letterList = aLetterList               # list of 6 letters on cube
        self.showingLetter = self.letterList[0]     # letter showing up


    # accessor methods

    # getLetterList: -> list of strings
    def getLetterList(self):
        return self.letterList

    # getShowingLetter -> string
    def getShowingLetter(self):
        return self.showingLetter


    # mutator methods

    # setLetterList: list of strings -> void
    def setLetterList(self,aLetterList):
        self.letterList = aLetterList


    # setShowingLetter: string -> void
    def setShowingLetter(self,aLetter):
        self.showingLetter = aLetter


    # special methods

    # __str__: -> string
    def __str__(self):
        return self.showingLetter

    # roll: -> void
    def roll(self):
        self.showingLetter = choice(self.letterList)
        
    
