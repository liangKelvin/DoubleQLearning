import blackjack
from pylab import *
import random
numEvaluationEpisodes = 2000

 
def run(numEvaluationEpisodes):
	returnSum = 0.0
	for episodeNum in range(numEvaluationEpisodes):
		G = 0
		gamma = 1
		# Choose a random action - 1 or 0
		action = random.randint(0,1)
		# initial state at the start of a new blackjack game
		state = blackjack.init()
		# Next state and reward from current state and action
		stateAction = blackjack.sample(state, action)
		reward = stateAction[0]
		state = stateAction[1]
		G = G + reward
		#print("reward1, newstate", reward, state)

		# go through every state in the game of blackJ
		while state != False :
			# Choose a random action - 1 or 0
			action = random.randint(0,1)
			# Next state and reward from current state and action
			stateAction = blackjack.sample(state, action)
			reward = stateAction[0]
			state = stateAction[1]
			#print("reward, newstate", reward, state)
			G = G + reward
			
		#print("Episode: ", episodeNum, "Return: ", G)
		returnSum = returnSum + G
	return returnSum / numEvaluationEpisodes
	
#run(numEvaluationEpisodes)