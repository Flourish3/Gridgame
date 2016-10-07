from grid import grid
from controller import controller
from agent import agent

gridSize = 5

grid = grid(gridSize)
controller = controller(gridSize)
agentSmith = agent(grid,controller)

iterations = 200000
for i in range(0,iterations):
	agentSmith.step()
	if i > 100000:
		#controller.setGreed(1)

print("Total reward: " +  str(agentSmith.getReward()) + " Iterations: " + str(iterations) + " Success rate: " + str(agentSmith.getReward()/iterations))
print("Points: " + str(grid.accPoints) + " Pen: " + str(grid.accPen) + " Sum: " + str(grid.accPoints - grid.accPen ))