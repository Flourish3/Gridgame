import random as r

class controller():
	gridWidth = 0
	gridHeight = 0
	treasurePlaces = 5
	damagedStates = 2
	nbrActions = 4

	greed = 0.2 #epsilon. greedy constant

	initQmatrix = 5

	totalStates = 0

	discount = 0.9	#Gamma
	stepSize = 0.2 	#Alpha
	
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

	def getBestAction(self,state):
		index = self.Q[0].index(state)
		actions = [self.Q[1][index],self.Q[2][index],self.Q[3][index],self.Q[4][index]]
		
		if r.random() > (1-self.greed):
			nextAction = actions.index(max(actions))
		else:
			nextAction = r.randint(0,3)
		

		#print(str(state) + " " + str(actions) + " " + str(nextAction))
		return nextAction
		
	def updateQmatrix(self,currentState,action,reward,previousState,previousAction):
		prevStateIndex = self.Q[0].index(previousState)
		nextStateIndex = self.Q[0].index(currentState)

		self.Q[previousAction+1][prevStateIndex] = (1-self.stepSize)*self.Q[action+1][prevStateIndex]+self.stepSize*(reward+self.discount*self.Q[action+1][nextStateIndex])

	def setGreed(self,newGreed):
		self.greed = newGreed