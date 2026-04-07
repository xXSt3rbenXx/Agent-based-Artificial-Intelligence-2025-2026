# Action structure (n_missionaries_on_boat, n_cannibals_on_boat)
possible_actions = [(0,1), (1,0), (2,0), (0,2), (1,1)] # l'azione è la tupla (nrdimissionaridatrasportare, nrdicannibalidatrasportare)

# State structure (n_missionaries_on_left_side, n_cannibals_on_left_side, boat_position)
    

class MissionariesAndCannibalsProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.possible_actions = possible_actions
        self.n_cannibals = 3
        self.n_missionaries = 3

    def decode_state(self, state):
        n_missionaries_dx = state[0]
        n_cannibals_dx = state[1]
        n_missionaries_lx = self.n_missionaries - n_missionaries_dx
        n_cannibals_lx = self.n_cannibals - n_cannibals_dx
        return n_missionaries_lx, n_cannibals_lx, n_missionaries_dx, n_cannibals_dx
    
    def get_missionaries_and_cannibals_number(self, state, side):
        n_missionaries_lx, n_cannibals_lx, n_missionaries_dx, n_cannibals_dx = self.decode_state(state)
        if side == 'left':
            return n_missionaries_lx, n_cannibals_lx
        elif side == 'right':
            return n_missionaries_dx, n_cannibals_dx
        else:
            raise ValueError("Side must be 'left' or 'right'")

    def decode_action(self, action):
        n_missionaries_on_boat = action[0]
        n_cannibals_on_boat = action[1]
        return n_missionaries_on_boat, n_cannibals_on_boat
    
    def allowed_state(self, state):
        n_missionaries_lx, n_cannibals_lx, n_missionaries_dx, n_cannibals_dx = self.decode_state(state)
        if (n_missionaries_lx > 0 and n_missionaries_lx < n_cannibals_lx) or (n_missionaries_dx > 0 and n_missionaries_dx < n_cannibals_dx):
            return False
        return True
    
    def boat_side(self, state):
        return 'right' if state[2] == 1 else 'left'

    def actions(self, state):
        actions = []
        boat_position = self.boat_side(state)
        for a in self.possible_actions:
            n_missionaries_on_boat, n_cannibals_on_boat = self.decode_action(a)
            # check if the boat on the right side
            n_missionaries_on_side, n_cannibals_on_side = self.get_missionaries_and_cannibals_number(state, boat_position)
            if n_cannibals_on_side >= n_cannibals_on_boat and n_missionaries_on_side >= n_missionaries_on_boat:
                new_state = self.result(state, a)
                if self.allowed_state(new_state):
                    actions.append(a)
        return actions

    def result(self, state, action):
        state = list(state)
        if self.boat_side(state) == 'right':
            state[0] = state[0] - action[0]
            state[1] = state[1] - action[1]
            state[2] = 0
        # if the booat is on the left side
        elif self.boat_side(state) == 'left':
            state[0] = state[0] + action[0]
            state[1] = state[1] + action[1]
            state[2] = 1
        return tuple(state)

    def action_cost(self, state, action):
        return 1

    def is_goal(self, state):
        return state == self.goal_state
