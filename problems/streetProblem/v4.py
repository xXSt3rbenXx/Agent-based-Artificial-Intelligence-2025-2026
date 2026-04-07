from problems.streetProblem.cities import *

CORATO = 'Corato'
RUVO = 'Ruvo'
TRANI = 'Trani'
MOLFETTA = 'Molfetta'
ANDRIA = 'Andria'
BARLETTA = 'Barletta'
MINERVINO = 'Minervino'
ALTAMURA = 'Altamura'
BISCEGLIE = 'Bisceglie'
MODUGNO = 'Modugno'
BARI = 'Bari'

STATES = [CORATO, RUVO, TRANI, MOLFETTA, ANDRIA, BARLETTA, MINERVINO, ALTAMURA, BISCEGLIE, MODUGNO, BARI]

class StreetProblem:
    def __init__(self, initial_state, goal_state):
        self._initial_state = initial_state
        self._goal_state = goal_state
        self.map = streets

    def actions(self, state):
        actions = []
        for city1, city2, _ in self.map:
            if city1 == state:
                actions.append(city2)
            elif city2 == state:
                actions.append(city1)
        return actions

    def result(self, state, action):
        for state1, state2, _ in self.map:
            if (state, action)  == (state1, state2):
                return state2
            if (state, action)  == (state2, state1):
                return state1
        raise ValueError(f"Invalid action {action} from state {state}")

    def step_cost(self, state, action):
        for state1, state2, cost in self.map:
            if (state, action)  == (state1, state2):
                return cost
            if (state, action)  == (state2, state1):
                return cost
        raise ValueError(f"Invalid action {action} from state {state}")

    def goal_condition(self, state):
        return state == self._goal_state

prob = StreetProblem(CORATO, RUVO)

for action in prob.map:
    c1, c2, cost = action
    if cost < cities_distance(c1, c2):
        print(f'Heuristic inconsistent for action {action}. Cost {cost}, h: {cities_distance(c1, c2)}')