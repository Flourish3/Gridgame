from grid import grid
from gridQController import gridQController
from agent import agent
import matplotlib.pyplot as plt

gridSize = 5

grid = grid(gridSize)
controller = gridQController(gridSize)
agentSmith = agent(grid,controller)

iterations = 200000

rewards = [0]*iterations

for i in range(0,iterations):
	agentSmith.step()
	if i > 100000:
		controller.setGreed(1)
	rewards[i] = agentSmith.getReward()

plt.plot(rewards)
plt.show()
print("Total reward: " +  str(agentSmith.getReward()) + " Iterations: " + str(iterations) + " Success rate: " + str(agentSmith.getReward()/iterations))