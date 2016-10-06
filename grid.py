class grid():
	#Class that handles the grid/game
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
		#Actions: 0 left 1 up 2 down 3 right
	R = []
	grid = []
	treasureState = 4
	gridSize = 0
	moveState = 0

	def __init__(self, size):
		self.gridSize = size
		self.initRewardMatrix()
		self.initGrid()
		print("Grid created")

	def initRewardMatrix(self):
		
		R =[0]

	def initGrid(self):
		for i in range(0,self.gridSize):
			self.grid.append([0]*self.gridSize)

	def setTreasure(self,t):
		if t == 0:
			self.grid[0][0] = 1
		elif t == 1:
			self.grid[0][self.gridSize-1] = 1
		elif t == 2:
			self.grid[self.gridSize-1][0] = 1
		elif t == 3:
			self.grid[self.gridSize-1][self.gridSize-1] = 1

		self.treasureState = t

	def getGridSize(self):
		return self.gridSize

	def left(self): #0
		print("left")

	def up(self): #1
		print("up")
	
	def down(self): #2
		print("down")
	
	def right(self): #3
		print("right")

