import random as r
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
	
	gridSize = 0
	moveState = 0
	agentX = 0
	agentY = 0
	treasureState = 4
	agentDamaged = 0
	treasureChance = 0.5
	monsterChance

	monster = [0,0,0,0,0]

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

	def step(self,action,state):
		#move the agent, then change the grid(treasure,monster)
		agentX = state[0]
		agentY = state[1]
		penelty = self.move(action)

		points = 0
		#check if agent is on treasure
		if self.agentX == 0 & self.agentY == 0 & self.treasureState == 0:
			points += 10
			treasureState = 4
		elif self.agentX == 0 & self.agentY == self.gridSize-1 & self.treasureState == 1:
			points += 10
			treasureState = 4
		elif self.agentX == self.gridSize-1 & self.agentY == 0 & self.treasureState == 2:
			po<nts += 10
			treasureState = 4
		elif self.agentX == self.gridSize-1 & self.agentY == self.gridSize-1 & self.treasureState == 3:
			points += 10
			treasureState = 4

		#Repair the agent
		if self.agentX == 0 & self.agentY == 1:
			agentDamaged = 0

		#Check monster
		if (self.agentX == 3 & self.agentY == 0 & monster[0] == 1) |
			(self.agentX == 3 & self.agentY == 1 & monster[1] == 1) |
			(self.agentX == 1 & self.agentY == 2 & monster[2] == 1) |
			(self.agentX == 3 & self.agentY == 3 & monster[3] == 1) |
			(self.agentX == 2 & self.agentY == 4 & monster[4] == 1):
			if agentDamaged == 1:
				penalty += 10
			agentDamaged = 1
			
		nextState = (agentX,agentY,treasureState,agentDamaged)
		#Spawn monsters
		if r.random > (1-monsterChance):
			index = r.randint(0,4)
			monsters[index] = !monsters[index] 

		#Spawn treasure
		if (self.treasureState != 4) & (r.random()> (1-self.treasureChance)):
			#spawn new treasure
			self.setTreasure(r.randint(0,3))


		totalReward = points - penelty
		return [totalReward,nextState]


	def getGridSize(self):
		return self.gridSize

	def move(self,action):
		
		if action == 0:
			return self.left()
		elif action == 1:
			return self.up()
		elif action == 2:
			return self.down()
		elif action == 3:
			return self.right()

	def left(self): #0
		if self.agentY == 0:
			#On the left row, can't move, penalty
			return 1
		elif self.agentX == 0 & (self.agentY == 1 | self.agentY == 2):
			#Standing to the right of wall, can't move into wall
			return 1
		elif self.agentX == 1 & self.agentY == 1:
			#Standing to the right of wall, can't move into wall
			return 1
		else:
			self.agentX -= 1
			return 0
		

	def up(self): #1
		if self.agentX == 0:
			#On the top row, can't move, penalty
			return 1
		
		self.agentY -= 1
		return 0
	
	def down(self): #2
		if self.agentX == self.gridSize-1:
			#On the top row, can't move, penalty
			return 1
		
		self.agentY += 1
		return 0
	
	def right(self): #3
		if self.agentY == self.gridSize-1:
			#On the right row, can't move, penalty
			return 1
		elif self.agentX == 0 & (self.agentY == 0 | self.agentY == 1):
			#Standing to the left of wall, can't move into wall
			return 1
		elif self.agentX == 1 & self.agentY == 0:
			#Standing to the left of wall, can't move into wall
			return 1
		else:
			self.agentX += 1
			return 0

