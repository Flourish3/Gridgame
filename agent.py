class agent():
	xPos = 2
	yPos = 2
	damaged = 0
	treasure = 4

	reward = 0
	grid = 0
	controller = 0
	def __init__(self,grid,controller):
		self.grid = grid
		self.controller = controller
		print("Agent created")

	def step(self):
		#Check with controller to see where we should go
		currentState = (self.xPos, self.yPos,self.treasure,self.damaged)
		Qstate = self.controller.getQstate(currentState)
		
		action = self.getBestAction(Qstate)
		nextState = self.grid.step(action,currentState)

	def getReward(self):
		return self.reward

	def getBestAction(self,Qstate):
		return 1