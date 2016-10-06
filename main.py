from grid import grid
from controller import controller
from agent import agent

gridSize = 5

grid = grid(gridSize)
controller = controller(gridSize)
agentSmith = agent(grid,controller)

iterations = 1000
for i in range(0,iterations):
	agentSmith.step()

print("Total reward: " +  str(agentSmith.getReward()) + " Iterations: " + str(iterations) + " Success rate: " + str(agentSmith.getReward()/iterations))