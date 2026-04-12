# Author: Alberto Carlo Maria Mancino
# Date: 2026-04-07

# In this problem, the state is represented as a tuple of 3 elements:
# liters in the first, second, and third container.
# Example: (8, 0, 2) -> first container is full, second is empty, third has 2 liters

# Action is a tuple (Input, Output), where Input and Output are the index of the container (0, 1, or 2), 3 for FULL, and 4 for EMPTY




class WaterJugProblem:

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.capacities = {0: 8, 1: 5, 2: 3}

    def all_actions(self):
        # Action is a tuple (Input, Output), where Input and Output are the index of the container (0, 1, or 2), 3 for FULL, and 4 for EMPTY
        containers = [0, 1, 2]
        actions = []
        # Pouring actions
        for c in containers:
            for d in containers:
                if c != d:
                    actions.append((c, d))

        # Filling and emptying actions
        for c in containers:
            actions.append((c, 3))  # Fill action
            actions.append((c, 4))  # Empty action
        return actions


    def actions(self, state):
        all_actions = self.all_actions()
        valid_actions = []
        for action in all_actions:
            result = self.result(state, action)
            # Only consider actions that change the state
            if result != state:
                valid_actions.append(action)

        return valid_actions

    def result(self, state, action):
        input, output = action
        if output == 3:  # Fill action
            newstate = list(state)
            newstate[input] = self.capacities[input]
            return tuple(newstate)
        elif output == 4:  # Empty action
            newstate = list(state)
            newstate[input] = 0
            return tuple(newstate)
        else:  # Pouring action
            newstate = list(state)
            amount_to_pour = min(state[input], self.capacities[output] - state[output])
            newstate[input] -= amount_to_pour
            newstate[output] += amount_to_pour
            return tuple(newstate)


    def is_goal(self, state):
        is_solution = False
        for i in range(len(state)):
            # Check if any container has exactly 4 liters
            if state[i] == 4:
                is_solution = True
        return is_solution

    def action_cost(self, state, action):

        # Each action has a constant cost of 1
        return 1