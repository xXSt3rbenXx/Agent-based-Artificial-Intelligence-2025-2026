import problems.streetProblem.cities as cities

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

        self.map = {}
        for city in cities.coords.keys():
            adjs = {'go_to_'+ city_name: cost for city_name, cost in cities.find_adjacent_cities(city).items()}
            self.map[city] = adjs

    def actions(self, state):
        return list(self.map[state].keys())

    def result(self, state, action):
        if action not in self.map[state]:
            raise ValueError(f"Invalid action {action} from state {state}")
        return action.replace('go_to_', '')

    def step_cost(self, state, action):
        return self.map[state][action]

    def goal_condition(self, state):
        return state == self._goal_state
