from random import *

def printIntro():
    print('This program simulates a game between two')
    print('There are two players, A and B')
    print('Probability(a number between 0 and 1) is used')


def getInputs():
    a = eval(input('What is the prob.player A wins?'))
    b = eval(input('What is the prob.player B wins?'))
    n = eval(input('How many games to simulate?'))
    return a, b, n


def simNGames(probA, probB, n):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = 'A'  # serving代表谁的球权
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    n = winsA + winsB
    print('Games simulated: {n} times.'.format(n=n))
    print('Wins for A: {winsA}({winsA_prob:0.1%})'.format(winsA=winsA, winsA_prob=winsA/n))
    print('Wins for B: {winsB}({winsB_prob:0.1%})'.format(winsB=winsB, winsB_prob=winsB/n))


def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(probA, probB, n)
    printSummary(winsA, winsB)


if __name__ == '__main__':
    main()
