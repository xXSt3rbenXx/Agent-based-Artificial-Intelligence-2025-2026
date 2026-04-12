# Author: Carotenuto Giusy
# Date: 2026-04-10


UP = 'up'
DOWN= 'down'
LEFT= 'left'
RIGHT= 'right'
PULISCI= 'pulisci'

class VacuumCleanerProblem:

    def __init__(self, initial_state, goal_state, celle_sporche):
        self.initial_state = (initial_state, tuple(celle_sporche))
        self.goal_state= goal_state

        self.map= {
            UP: (-1, 0),
            DOWN: (+1, 0),
            LEFT: (0,-1),
            RIGHT: (1, 0),
            PULISCI: (0,0)
        }


    def actions(self, state):
        (x, y), celle_sporche_attuali = state
        azioni = []

        for action in self.map:
            dx, dy= self.map[action]
            new_x= x + dx
            new_y = y + dy
            if new_x !=2 and new_y!=2 and new_x!=-1 and new_y!=-1:
                azioni.append(action)

        return azioni

    def result(self, state, action):
        (x, y), celle_sporche_attuali = state
        dx, dy = self.map[action]
        new_x = x + dx
        new_y = y + dy
        copia_celle = list(celle_sporche_attuali)
        if action== PULISCI and (x,y) in copia_celle:
            copia_celle.remove((new_x, new_y))
        if new_x != 2 and new_y != 2 and new_x != -1 and new_y != -1:
            return ((new_x, new_y), tuple(copia_celle))
        else:
            return state

    def is_goal(self, state):
        (x, y), celle_sporche_attuali = state
        if len(celle_sporche_attuali) == len(self.goal_state):
            return True
        return False

    def action_cost(self, state, action):
        return 1
