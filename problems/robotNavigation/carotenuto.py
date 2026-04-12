# Author: Carotenuto Giusy
# Date: 2026-04-10


#realizzo il problema considerando un'astrazione del problema

UP= 'up'
DOWN= 'down'
LEFT= 'left'
RIGHT= 'right'

class RobotNavigationProblem:

#un problema è definito dallo state-space, stato iniziale, goal condition (o sets), azioni e model transition
    def __init__(self, initial_state, goal_state, ostacolo):

        self.initial_state= initial_state
        self.goal_state= goal_state
        self.ostacolo= ostacolo

        self.map= {
            UP:    (0, -1),
            DOWN:  (0, +1),
            LEFT:  (-1, 0),
            RIGHT: (1, 0)
        }


    def actions(self, state):
        azioni_possibili = []
        for i in [UP, DOWN, LEFT, RIGHT]:
            action= self.map[i]
            x= (state[0] + action[0])
            y = state[1] + action[1]
            new_state= (x,y)
            if new_state not in self.ostacolo and (new_state[0]!=0 and new_state[0]!=3) and (new_state[1]!=0 and new_state[1]!=3):
                azioni_possibili.append(i)
        return azioni_possibili


    def result(self, state, action):
        azione= self.map[action]
        x = state[0] + azione[0]
        y = state[1] + azione[1]
        new_state = (x, y)

        if new_state not in self.ostacolo and (new_state[0]!=0 and new_state[0]!=3) and (new_state[1]!=0 and new_state[1]!=3):
            return new_state
        else:
            return state

    def action_cost(self, state, azione):
        if azione == UP or azione== DOWN:
            return 2
        else:
            return 1

    def is_goal(self, state):
        return state== self.goal_state



