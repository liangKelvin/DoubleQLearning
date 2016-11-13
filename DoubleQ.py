import blackjack
from pylab import *
from numpy import *
import random
 
numEpisodes = 1000000

alpha = 0.001 # Best Value 0.052
epsilon = 0.01 # Best Value 0.022
gamma = 1

Q1 = 0.00001*rand(182,2)
Q2 = 0.00001*rand(182,2)
Q1[181, :] = 0
Q2[181, :] = 0
qtotal = Q1 + Q2

# Greedy policy in sum of two action values
def policy(s) :
	qTotal = Q1 + Q2
	return argmax(qTotal[s, :])

def learn(alpha, eps, numTrainingEpisodes):
	returnSum = 0.0
	for episodeNum in range(numTrainingEpisodes):
		G = 0
		s = blackjack.init() # initial state
		# pick a random number between 0 and 1
		# this represents the random greedy probability
		i = random.uniform(0,1) 
		
		# use random policy from part 1
		if i < epsilon :
			a = random.randint(0,1)

		else :
			# Greedy policy in sum of two action values
			qTotal = Q1 + Q2
			a = argmax(qTotal[s, :])

		# Next state and reward from current state and action	
		stateAction = blackjack.sample(s,a)
		newState = stateAction[1]
		reward = stateAction[0]

		if newState == False :
			newState = 181

		#probability of 0.5 for update
		p = random.randint(0,1)
		# update q1
		if p == 0 :
			Q1[s,a] = Q1[s,a] + alpha * (reward + (gamma * Q2[newState, argmax(Q1[newState, :])]) - Q1[s,a])
		# update q2
		elif p == 1 :
			Q2[s,a] = Q2[s,a] + alpha * (reward + (gamma * Q1[newState, argmax(Q2[newState, :])]) - Q2[s,a])
		# update newState to False - terminal state
		if newState == 181 :
			newState = False 
		

		s = newState
		G = G + reward

		while s != False :

			i = random.uniform(0,1) 
			
			# use random policy from part 1
			if i < epsilon :
				a = random.randint(0,1)
				
			else :
				qTotal = Q1 + Q2
				a = argmax(qTotal[s, :])

			stateAction = blackjack.sample(s,a)
			newState = stateAction[1]
			reward = stateAction[0]
			# allow for terminal state announcement
			if newState == False :
				newState = 181

			#probabilty of 0.5 for update
			p = random.randint(0,1)
			# update q1
			if p == 0 :
				Q1[s,a] = Q1[s,a] + alpha * (reward + (gamma * Q2[newState, argmax(Q1[newState, :])]) - Q1[s,a])
			# update q2
			elif p == 1 :
				Q2[s,a] = Q2[s,a] + alpha * (reward + (gamma * Q1[newState, argmax(Q2[newState, :])]) - Q2[s,a])

			# reset the state assignment
			if newState == 181 :
				newState = False 
			
			s = newState
			G = G + reward
			
		#print("Episode: ", episodeNum, "Return: ", G)
		returnSum = returnSum + G
		#if episodeNum % 10000 == 0 and episodeNum != 0:
			#print("Average return so far: ", returnSum / episodeNum)
	#blackjack.printPolicyToFile(policy)


def evaluate(numEvaluationEpisodes):
	returnSum = 0.0
	for episodeNum in range(numEvaluationEpisodes):
		G = 0
		s = blackjack.init() # initial state
		# Choose an action with greedy policy
		a = policy(s)
		# Next state and reward from current state and action
		stateAction = blackjack.sample(s,a)
		newState = stateAction[1]
		reward = stateAction[0]
		G = G + reward

	# go through every state in the game of blackJ
		while newState != False :

			a = policy(newState)
			# Next state and reward from current state and action
			stateAction = blackjack.sample(newState, a)
			reward = stateAction[0]
			newState = stateAction[1]
			G = G + reward
		
		# Use deterministic policy from Q1 and Q2 to run a number of
		# episodes without updates. Return average return of episodes.
		returnSum = returnSum + G
	return returnSum / numEvaluationEpisodes


 
#learn(alpha, epsilon, numEpisodes)
#x = evaluate(numEpisodes)
""""
Part 2 results
Average return observed when 
alpha = 0.001
eps = 0.01
numTrainingEpisodes = 1,000,000
Learning:
avgReturn = -0.067753
Evaluation:
Deterministic avgReturn = -0.0300204
"""
#print("return: ", x)
