import mdp, util

from learningAgents import ValueEstimationAgent

class class ValueIterationAgent:
    def __init__(self, mdp, discount=0.9, iterations=100):
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # Dictionary to store state values

        for _ in range(iterations):
            new_values = util.Counter()  # Temporary dictionary for updated values
            for state in self.mdp.getStates():
                if not self.mdp.isTerminal(state):
                    # Compute Q-value for each action
                    q_values = [self.computeQValue(state, action) for action in self.mdp.getPossibleActions(state)]
                    new_values[state] = max(q_values)  # Update value with maximum Q-value
            self.values = new_values  # Update values for next iteration

    def computeQValue(self, state, action):
        q_value = 0
        for next_state, prob in self.mdp.getTransitionStatesAndProbs(state, action):
            reward = self.mdp.getReward(state, action, next_state)
            q_value += prob * (reward + self.discount * self.values[next_state])
        return q_value

    def getValue(self, state):
        return self.values[state]

    def getPolicy(self, state):
        if self.mdp.isTerminal(state):
            return None
        actions = self.mdp.getPossibleActions(state)
        return max(actions, key=lambda action: self.computeQValue(state, action))

        """
                """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
