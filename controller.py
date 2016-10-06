#import numpy as np

class controller():
	gridWidth = 5
	gridHeight = 5
	treasurePlaces = 5
	damagedStates = 2
	nbrActions = 4

	initQmatrix = 0

	totalStates = gridHeight*gridWidth*treasurePlaces*damagedStates
	
	Q = []
	R = []
	def __init__(self):
		self.Q = [[self.initQmatrix]*self.totalStates,
				  [self.initQmatrix]*self.totalStates,
				  [self.initQmatrix]*self.totalStates,
				  [self.initQmatrix]*self.totalStates]
		initRewardMatrix(

	def initRewardMatrix(self):
		#Grid game
		#__________________
		#|P0||R ||  |  |P1|
		#|  ||  | M |  |  |
		#|  |   |   |  |M |
		#|M | M |   |M |  |
		#|P2|   |   |  |P3|
		#P4 - no prize
		#10 rewards for treasure
		#Monsters appear anytime on M places
		#Agent is damaged if it lands on monster
		#-10 if it lands on montster when damaged
		#Repaired when on R

c = controller() 