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

        self.map = {
            CORATO: {TRANI: 12, BISCEGLIE: 8, RUVO: 10, ALTAMURA: 35, ANDRIA: 15},
            BARLETTA: {TRANI: 11, ANDRIA: 10, MINERVINO: 25},
            ANDRIA: {CORATO: 15, BARLETTA: 10, MINERVINO: 20},
            MINERVINO: {BARLETTA: 25, ANDRIA: 20, ALTAMURA: 30},
            TRANI: {CORATO: 12, BISCEGLIE: 6, BARLETTA: 11},
            BISCEGLIE: {TRANI: 6, MOLFETTA: 7, CORATO: 8},
            MOLFETTA: {BISCEGLIE: 7, RUVO: 14, MODUGNO: 20, BARI: 25},
            RUVO: {CORATO: 10, MOLFETTA: 14, MODUGNO: 18, ALTAMURA: 22},
            ALTAMURA: {MINERVINO: 30, CORATO: 35, RUVO: 22, MODUGNO: 28, BARI: 40},
            MODUGNO: {MOLFETTA: 20, RUVO: 18, ALTAMURA: 28, BARI: 10},
            BARI: {MOLFETTA: 25, MODUGNO: 10, ALTAMURA: 40},
        }

    def actions(self, state):
        return list(self.map[state].keys())

    def result(self, state, action):
        if action not in self.map[state]:
            raise ValueError(f"Invalid action {action} from state {state}")
        return action

    def step_cost(self, state, action):
        return self.map[state][action]

    def goal_condition(self, state):
        return state == self._goal_state