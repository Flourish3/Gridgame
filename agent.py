class agent():
	xPos = 0
	yPos = 0
	damaged = 0
	isTreasure = 0

	reward = 0
	grid = 0
	controller = 0
	def __init__(self,grid,controller):
		self.grid = grid
		self.controller = controller
		print("Agent created")

	def step(self):
		print("Step")

	def getReward(self):
		return self.reward