import blackjack
from pylab import *

def readPolicy(filename):
    policyArray = zeros((181,), dtype=int)
    f = open(filename)
    for usableAce in [1, 0]:
        f.readline(), 
        f.readline(), 
        for playerSum in range(20, 11, -1):
            for dealerCard in range(1, 11):
                e = 1 + (90 if usableAce else 0) + \
                        9 * (dealerCard - 1) + (playerSum - 12)
                policyArray[e] = 0 if (f.read(2) == 'S ') else 1
            f.readline(), 
        f.readline(), 
    return policyArray
    
def assessPolicy(policy, numEpisodes):
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        S = blackjack.init()
        while S is not False:
            A = policy(S)
            R, Sprime = blackjack.sample(S, A)
            G += R
            S = Sprime
        returnSum += G
    return returnSum / numEpisodes

policyArray = readPolicy('policy.txt')

def policy(s):
    return policyArray[s]


if __name__ == '__main__':
    blackjack.printPolicy(policy)
    print("Average return of policy:", assessPolicy(policy, 1000000))
