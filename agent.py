class agent():
	xPos = 2
	yPos = 2
	damaged = 0
	treasure = 4

	reward = 0
	grid = 0
	controller = 0

	previousState = 0
	previousAction = 0

	def __init__(self,grid,controller):
		self.previousState = (self.xPos,self.yPos,self.treasure,self.damaged)
		self.grid = grid
		self.controller = controller
		print("Agent created")

	def step(self):
		#Check with controller to see where we should go
		#currentState = (self.xPos, self.yPos,self.treasure,self.damaged)
		
		#Get best action
		action = self.controller.getBestAction(self.previousState)
		
		#Perform the action
		gridInfo = self.grid.step(action,self.previousState)
		rewardFromAction = gridInfo[0]
		self.reward += rewardFromAction
		currentState = gridInfo[1]
		#print(str(self.previousState) + " " + str(action))
		
		#Update Q-matrix		
		self.controller.updateQmatrix(currentState,action,rewardFromAction,self.previousState,self.previousAction)

		#Update previous states
		self.previousState = currentState
		self.previousAction = action

	def getReward(self):
		return self.reward