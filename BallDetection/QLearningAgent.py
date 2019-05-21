from random import randint
from random import random


class QLearningAgent:
    a = 0.01  # learnrate
    epsilon = 0.1  # 10% for epsilon-greedy
    gamma = 0.9  # discount factor
    q  = []
    possibleActions = 0

    def _init_(self, actions, states):
        possibleActions = actions
        for i in range(states):
            obj = [];
            #Three actions: left, stay, right
            for j in range(actions):
                obj.append(float(randint(0,1)))
                self.q.append(obj)



    def learn(self, state, nextState, action, reward):
        self.q[state][action] += self.a * (reward + self.gamma * (self.q[nextState][self.actionWithBestRating(nextState)] - self.q[state][action]))


    def chooseAction(self, state):
        action = 0
        e = random()
        # epsilon-greedy
        if (e < self.epsilon):
            # choose random action
            action = randint(self.possibleActions)
        else:
            # choose action with highest q value
            action = actionWithBestRating(state)
        return a


    def actionWithBestRating(self, state):
        max = 0
        index = 0
        for i in range(self.possibleActions):
            if self.q[state][i] > max:
                max = q[state][i]
                index = i;

        return index


    def saveToFile(self):
        # save q table to file
        return 0

    def readFile(self):
        # read q values from file and initialize q table
        return 0


