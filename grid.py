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
	
	gridSize = 0
	agentX = 2
	agentY = 2
	treasureState = 4
	agentDamaged = 0
	treasureChance = 0.5
	monsterChance = 0.5

	totalStates = 250

	monsters = [r.random()<monsterChance,r.random()<monsterChance,r.random()<monsterChance,r.random()<monsterChance,r.random()<monsterChance]

	def __init__(self, size):
		self.gridSize = size
		print("Grid created")

	def step(self,action,state):
		#move the agent, then change the grid(treasure,monster)
		agentX = state[0]
		agentY = state[1]
		penelty = self.move(action)

		points = 0
		#check if agent is on treasure
		if self.agentX == 0 and self.agentY == 0 and self.treasureState == 0:
			points += 10
			self.treasureState = 4
		elif self.agentX == 0 and self.agentY == self.gridSize-1 and self.treasureState == 1:
			points += 10
			self.treasureState = 4
		elif self.agentX == self.gridSize-1 and self.agentY == 0 and  self.treasureState == 2:
			points += 10
			self.treasureState = 4
		elif self.agentX == self.gridSize-1 and  self.agentY == self.gridSize-1 and  self.treasureState == 3:
			points += 10
			self.treasureState = 4

		#Repair the agent
		if self.agentX == 0 and  self.agentY == 1:
			self.agentDamaged = 0

		#Check monster
		if ((self.agentX == 3) and (self.agentY == 0) and  (self.monsters[0] == 1)) or (self.agentX == 3 and  self.agentY == 1 and  self.monsters[1] == 1) or (self.agentX == 1 and  self.agentY == 2 and  self.monsters[2] == 1) or (self.agentX == 3 and  self.agentY == 3 and  self.monsters[3] == 1) or	(self.agentX == 2 and  self.agentY == 4 and  self.monsters[4] == 1):
			if self.agentDamaged == 1:
				penelty += 10
			self.agentDamaged = 1
			
		nextState = (self.agentX,self.agentY,self.treasureState,self.agentDamaged)
		#Spawn monsters
		monsters = [r.random()<self.monsterChance,r.random()<self.monsterChance,r.random()<self.monsterChance,r.random()<self.monsterChance,r.random()<self.monsterChance]
		
		#Spawn treasure
		if (self.treasureState == 4) and (r.random() < self.treasureChance):
			#spawn new treasure
			self.treasureState = r.randint(0,3)

		totalReward = points - penelty
		#print(totalReward)
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
		else:
			print("WTF?")

	def left(self): #0
		if self.agentY == 0:
			#On the left row, can't move, penalty
			return 1
		elif self.agentX == 0 and  (self.agentY == 1 or self.agentY == 2):
			#Standing to the right of wall, can't move into wall
			return 1
		elif self.agentX == 1 and  self.agentY == 1:
			#Standing to the right of wall, can't move into wall
			return 1
		else:
			self.agentY -= 1
			return 0
		

	def up(self): #1
		if self.agentX == 0:
			#On the top row, can't move, penalty
			return 1
		else:
			self.agentX -= 1
			return 0
	
	def down(self): #2
		if self.agentX == self.gridSize-1:
			#On the top row, can't move, penalty
			return 1
		else:
			self.agentX += 1
			return 0
	
	def right(self): #3
		if self.agentY == self.gridSize-1:
			#On the right row, can't move, penalty
			return 1
		elif self.agentX == 0 and  (self.agentY == 0 or self.agentY == 1):
			#Standing to the left of wall, can't move into wall
			return 1
		elif self.agentX == 1 and  self.agentY == 0:
			#Standing to the left of wall, can't move into wall
			return 1
		else:
			self.agentY += 1
			return 0

