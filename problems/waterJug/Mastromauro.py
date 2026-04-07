# Author: Mastromauro Camilla
# Date: 2026-03-31

# In this problem, the state is represented as a tuple of 3 elements:
# liters in the first, second, and third container.
# Example: (8, 0, 2) -> first container is full, second is empty, third has 2 liters

# Allowed actions:
FULL_A = 'Full_A'
FULL_B = 'Full_B'
FULL_C = 'Full_C'
EMPTY_A = 'Empty_A'
EMPTY_B = 'Empty_B'
EMPTY_C = 'Empty_C'
A_TO_B = 'A_TO_B'
B_TO_A = 'B_TO_A'
C_TO_B = 'C_TO_B'
C_TO_A = 'C_TO_A'
B_TO_C = 'B_TO_C'
A_TO_C = 'A_TO_C'


class WaterJugProblem:

    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.capacities = {0: 8, 1: 5, 2: 3}
        self.actionsFULLEMPTY = {0: [FULL_A, EMPTY_A], 1: [FULL_B, EMPTY_B], 2: [FULL_C, EMPTY_C]}
        self.actionsFROMTO = {0: [0, A_TO_B, A_TO_C], 1: [B_TO_A, 0, B_TO_C], 2: [C_TO_A, C_TO_B, 0]}

    def actions(self, state):
        actions = []
        for container in range(len(state)):

            # If the container is not full, it can be filled
            if state[container] < self.capacities[container]:
                actions.append(self.actionsFULLEMPTY[container][0])

            # If the container is not empty, it can be emptied
            if state[container] != 0:
                actions.append(self.actionsFULLEMPTY[container][1])

            for j in range(len(state)):
                if container != j:

                    # If source has water and destination is not full,
                    # it is possible to pour from one to another
                    if state[container] > 0 and state[j] < self.capacities[j]:
                        actions.append(self.actionsFROMTO[container][j])

        return actions

    def result(self, state, action):
        newstate = list(state)

        for container in self.capacities:

            if action in self.actionsFULLEMPTY[container]:

                # If action is FULL, set container to its maximum capacity
                if action == self.actionsFULLEMPTY[container][0]:
                    newstate[container] = self.capacities[container]

                # If action is EMPTY, set container to 0
                elif action == self.actionsFULLEMPTY[container][1]:
                    newstate[container] = 0

            elif action in self.actionsFROMTO[container]:

                for i in range(len(state)):

                    if action == self.actionsFROMTO[container][i]:

                        # If total liters exceed destination capacity
                        if state[container] + state[i] >= self.capacities[i]:

                            # Destination is filled to max
                            newstate[i] = self.capacities[i]

                            # Source loses the transferred amount
                            newstate[container] = state[container] - (self.capacities[i] - state[i])

                        # If source does not have enough to fill destination
                        elif (self.capacities[i] - state[i]) > state[container]:

                            # Source becomes empty
                            newstate[container] = 0

                            # Destination increases but is not full
                            newstate[i] = state[i] + state[container]

                        # If source has exactly what destination needs
                        elif (self.capacities[i] - state[i]) == state[container]:

                            # Source becomes empty
                            newstate[container] = 0

                            # Destination becomes full
                            newstate[i] = self.capacities[i]

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