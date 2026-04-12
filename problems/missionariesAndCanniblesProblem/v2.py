# Action structure (n_missionaries_on_boat, n_cannibals_on_boat, 0)
# State structure (n_missionaries_on_left_side, n_cannibals_on_left_side, boat_position)
    
def possible_actions(boat_space):
    actions = []
    for x in range(boat_space + 1):
        for y in range(boat_space + 1 - x):
            if x == 0 and y == 0:
                continue
            if (x+y) <= boat_space:
                actions.append((x, y, 0))
    return actions


class MissionariesAndCannibalsProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.n_cannibals = 3
        self.n_missionaries = 3
        self.boat_space = 2
        self.possible_actions = possible_actions(self.boat_space)


    def decode_action(self, action):
        n_missionaries_on_boat = action[0]
        n_cannibals_on_boat = action[1]
        return n_missionaries_on_boat, n_cannibals_on_boat
    
    def allowed_state(self, state):
        x, y, _ = state
        if x < 0 or x > self.n_missionaries:
            return False
        if y < 0 or y > self.n_cannibals:
            return False
        # more cannibals than missionaries on the right side
        if y > x and x > 0:
            return False
        if (self.n_cannibals - y) > (self.n_missionaries - x) and (self.n_missionaries - x) > 0:
            return False
        return True
    
    def boat_side(self, state):
        return 'right' if state[2] == 1 else 'left'

    def actions(self, state):
        actions = []
        for a in self.possible_actions:
            new_state = self.result(state, a)
            if self.allowed_state(new_state):
                actions.append(a)
        return actions

    def result(self, state, action):
        new_state = list(state)
        for i in range(2):
            if self.boat_side(state) == 'right':
                new_state[i] = state[i] - action[i]
            elif self.boat_side(state) == 'left':
                new_state[i] = state[i] + action[i]
            else:
                raise ValueError("Invalid boat position")
        # toggle boat position
        new_state[2] = 1 - state[2]
        return tuple(new_state)

    def action_cost(self, state, action):
        return 1

    def is_goal(self, state):
        return state == self.goal_state
