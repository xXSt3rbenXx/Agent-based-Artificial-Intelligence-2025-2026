# Author: Carotenuto Giusy
# Date: 2026-04-10


import copy
UP= 'up'
DOWN= 'down'
LEFT= 'left'
RIGHT= 'right'

class EightTiles:

#un problema è definito dallo state-space, stato iniziale, goal condition (o sets), azioni e model transition
    def __init__(self, initial_state, goal_state):

        self.initial_state= initial_state
        self.goal_state= goal_state

        self.map= {
            UP: -1,
            DOWN: +1,
            LEFT: -1,
            RIGHT: +1
        }


    def actions(self, state):
        x, y = self.empty_tile_coords(state)
        azioni_possibili= []
        if (x!=2):
            azioni_possibili.append(DOWN)
        if (x!=0):
            azioni_possibili.append(UP)
        if (y!=2):
            azioni_possibili.append(RIGHT)
        if (y!=0):
            azioni_possibili.append(LEFT)

        return azioni_possibili
    
    def empty_tile_coords(self, state):
        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    return i, j
        raise KeyError('Empty tile not found')

    def result(self, state_true, action):
        state= copy.deepcopy(state_true)
        dx= self.map[action]
        x, y = self.empty_tile_coords(state)

        if action == UP or action == DOWN:
            new_x = x + dx
            state = [list(row) for row in state]
            temp = state[new_x][y]
            state[new_x][y] = state[x][y]
            state[x][y] = temp
            state = tuple(tuple(row) for row in state)

        if action == LEFT or action == RIGHT:
            new_y = y + dx
            state = [list(row) for row in state]
            temp = state[x][new_y]
            state[x][new_y] = state[x][y]
            state[x][y] = temp
            state = tuple(tuple(row) for row in state)

        return state


    def is_goal(self, state):
        return (state==self.goal_state)
    
    def action_cost(self, state, action):
        return 1

