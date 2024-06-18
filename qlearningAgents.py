# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    def __init__(self, **args):
        ReinforcementAgent.__init__(self, **args)
        self.qvalues = {}  # Q-values for (state, action) pairs

    def getQValue(self, state, action):
        if (state, action) not in self.qvalues:
            return 0.0
        else:
            return self.qvalues[(state, action)]

    def computeValueFromQValues(self, state):
        possibleActions = self.getLegalActions(state)
        if len(possibleActions) == 0:
            return 0

        value = None
        result = None
        for action in possibleActions:
            temp = self.getQValue(state, action)
            if value is None or temp > value:
                value = temp
                result = action

        if value is None:
            value = 0
        return value

    def computeActionFromQValues(self, state):
        # Implement this method...
        pass

    def getAction(self, state):
        # Implement this method...
        pass

    def update(self, state, action, nextState, reward):
        


    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    def __init__(self, **args):
        QLearningAgent.__init__(self, **args)

    def computeActionFromQValues(self, state):
        """
        Compute the best action to take in a state.
        """
        possibleActions = self.getLegalActions(state)
        if len(possibleActions) == 0:
            return None

        bestAction = None
        bestValue = float("-inf")
        for action in possibleActions:
            qValue = self.getQValue(state, action)
            if qValue > bestValue:
                bestValue = qValue
                bestAction = action

        return bestAction

    def getAction(self, state):
        """
        Returns the action to take based on the current state.
        """
        legalActions = self.getLegalActions(state)
        if len(legalActions) == 0:
            return None

        if util.flipCoin(self.epsilon):
            return random.choice(legalActions)
        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        """
        Update Q-values based on the observed transition.
        """
       

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
