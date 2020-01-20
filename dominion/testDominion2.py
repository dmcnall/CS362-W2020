# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:33:01 2020

@author: mcnalld
"""

import Dominion
import random
from collections import defaultdict

#Get player names
testUtility.GetPlayerNames()

# testcase 2: redefined supplyNum = 0.

supplyNum = 0 
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
