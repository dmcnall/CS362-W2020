# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:33:01 2020

@author: mcnalld
"""

import Dominion
import random
from collections import defaultdict

def GetPlayerNames():
	#Get player names
	player_names = ["Annie","*Ben","*Carla"]
	return player_names

def SetCurseVictory():
	#Set number of curses and victory cards
	player_names = GetPlayerNames()

	if len(player_names)>2:
    		nV=12
	else:
    		nV=8
	nC = -10 + 10 * len(player_names)
	return nC, nV
	
def GetBoxes(nV):
	#Define box

	box = {}
	box["Woodcutter"]=[Dominion.Woodcutter()]*10
	box["Smithy"]=[Dominion.Smithy()]*10
	box["Laboratory"]=[Dominion.Laboratory()]*10
	box["Village"]=[Dominion.Village()]*10
	box["Festival"]=[Dominion.Festival()]*10
	box["Market"]=[Dominion.Market()]*10
	box["Chancellor"]=[Dominion.Chancellor()]*10
	box["Workshop"]=[Dominion.Workshop()]*10	
	box["Moneylender"]=[Dominion.Moneylender()]*10
	box["Chapel"]=[Dominion.Chapel()]*10
	box["Cellar"]=[Dominion.Cellar()]*10
	box["Remodel"]=[Dominion.Remodel()]*10
	box["Adventurer"]=[Dominion.Adventurer()]*10
	box["Feast"]=[Dominion.Feast()]*10
	box["Mine"]=[Dominion.Mine()]*10
	box["Library"]=[Dominion.Library()]*10
	box["Gardens"]=[Dominion.Gardens()]*nV
	box["Moat"]=[Dominion.Moat()]*10
	box["Council Room"]=[Dominion.Council_Room()]*10
	box["Witch"]=[Dominion.Witch()]*10
	box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
	box["Militia"]=[Dominion.Militia()]*10
	box["Spy"]=[Dominion.Spy()]*10
	box["Thief"]=[Dominion.Thief()]*10
	box["Throne Room"]=[Dominion.Throne_Room()]*10
	return box

def SetRandSupply(supplyNum) 
	#Pick 10 cards from box to be in the supply.
	boxlist = [k for k in box]
	random.shuffle(boxlist)
	randomnum = boxlist[:num]
	supply = defaultdict(list,[(k,box[k]) for k in randomnum])
	return supply

def GetSupply(nV, nC):
	#The supply always has these cards
	supply = SetRandSupply(num)
	supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
	supply["Silver"]=[Dominion.Silver()]*40
	supply["Gold"]=[Dominion.Gold()]*30
	supply["Estate"]=[Dominion.Estate()]*nV
	supply["Duchy"]=[Dominion.Duchy()]*nV
	supply["Province"]=[Dominion.Province()]*nV
	supply["Curse"]=[Dominion.Curse()]*nC
	return supply

def InitializeTrash():
	#initialize the trash
	trash = []
	return trash

def GetPlayers():
	#Costruct the Player objects
	players = []
	player_names = GetPlayerNames()
	for name in player_names:
	    if name[0]=="*":
	        players.append(Dominion.ComputerPlayer(name[1:]))
	    elif name[0]=="^":
       		 players.append(Dominion.TablePlayer(name[1:]))
    		else:
       		 players.append(Dominion.Player(name))
	return players 


def PlayGame():
	#Play the game
	supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}
	supply = GetSupply()
	players = GetPlayers()
	InitializeTrash()

	turn  = 0
	while not Dominion.gameover(supply):
    	turn += 1    
    	print("\r")    
    	for value in supply_order:
       		print (value)
       		 for stack in supply_order[value]:
        	    if stack in supply:
        	        print (stack, len(supply[stack]))
    	print("\r")
   		 for player in players:
   	     print (player.name,player.calcpoints())
  	  print ("\rStart of turn " + str(turn))    
 		   for player in players:
	        if not Dominion.gameover(supply):
        	    print("\r")
        	    player.turn(players,supply,trash)
        return     

#Final score
def GameSet():

	dcs=Dominion.cardsummaries(players)
	vp=dcs.loc['VICTORY POINTS']
	vpmax=vp.max()
	winners=[]
	for i in vp.index:
    		if vp.loc[i]==vpmax:
       		 winners.append(i)
	if len(winners)>1:
   	 winstring= ' and '.join(winners) + ' win!'
	else:
	    winstring = ' '.join([winners[0],'wins!'])

	print("\nGAME OVER!!!\n"+winstring+"\n")
	print(dcs)
	return 


#Get player names
GetPlayerNames()

#Set curses and victory cards (nC and nV respectively)
nC, nV = SetCurseVictory()

#Get Boxes
GetBoxes(nV)

#Pick n(=10) cards from box to be in the supply.
SetRandSupply(10)

#The supply always has these cards
GetSupply(nC, nV)

#Costruct the Player objects
SetPlayers()

#Play the game
PlayGame()

#Final score
GameSet()
