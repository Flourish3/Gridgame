import numpy as np

class controller():
	gridWidth = 0
	gridHeight = 0
	treasurePlaces = 5
	damagedStates = 2
	nbrActions = 4

	initQmatrix = 0

	totalStates = 0
	
	Q = []
	R = []
	def __init__(self,gridSize):
		self.gridWidth = gridSize	
		self.gridHeight = gridSize
		self.totalStates = self.gridHeight*self.gridWidth*self.treasurePlaces*self.damagedStates
		self.initQ()

		print("Controller created")
	

	def initQ(self):
		tmp = [0]*self.totalStates
		x = 0
		for i in range(0,self.gridWidth):
			for j in range(0,self.gridHeight):
				for k in range(0,self.treasurePlaces):
					for l in range(0,self.damagedStates):
						tmp[x] = (i,j,k,l)
						x+=1
		self.Q = [tmp,
				  [self.initQmatrix]*self.totalStates,
				  [self.initQmatrix]*self.totalStates,
				  [self.initQmatrix]*self.totalStates,
				  [self.initQmatrix]*self.totalStates] 