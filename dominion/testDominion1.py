# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:33:01 2020

@author: mcnalld
"""

import Dominion
import random
from collections import defaultdict

#testcase 1: redefined GetPlayerNames with the following two definitions in testUtility.py: 

# definition 1:
def GetPlayerNames():
	#Get player names
	player_names = ["A"]
	return player_names

# definition 2:
def GetPlayerNames():
	#Get player names
	player_names = []
	return player_names

supplyNum = 10

#Set curses and victory cards (nC and nV respectively)
nC, nV = testUtility.SetCurseVictory()

#Get Boxes
testUtility.GetBoxes(nV)

#Pick n(=10)  default
testUtility.SetRandSupply(supplyNum)

#The supply always has these cards
testUtility.GetSupply(nC, nV)

#Costruct the Player objects
testUtility.GetPlayers()

#Play the game
testUtility.PlayGame()

#Final score
testUtility.GameSet()
