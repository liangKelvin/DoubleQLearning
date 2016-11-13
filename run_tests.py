#!/usr/bin/env python3

import DoubleQ
import randomPolicy
import assessPolicy
import time

if __name__ == '__main__':
    p1e = 10000
    p2l = 1000000
    p2e = 1000000
    p3e = 1000000
    avgReturn = randomPolicy.run(p1e)
    print("Average return for part 1: ", avgReturn)
    start = time.time()
    DoubleQ.learn(alpha=0.001, eps=0.01, numTrainingEpisodes=p2l)
    print("Part 2 learning complete.")
    avgReturn = DoubleQ.evaluate(numEvaluationEpisodes=p2e)
    end = time.time()
    print("Part 2 evaluation complete.")
    print("Average return for part 2: ", avgReturn)
    print("Time: ", end - start)
    with open('part3.txt', 'r') as fp:
        (_, _, _, averageReturn, _) = fp.read().split('\n')
    print("Reported average return: ", float(averageReturn[10:]))
    policyArray = assessPolicy.readPolicy("policy.txt")
    print(assessPolicy.assessPolicy(lambda S: policyArray[S], p3e))

