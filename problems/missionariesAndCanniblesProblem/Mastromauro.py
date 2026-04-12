# Author: Mastromauro Camilla
# Date: 2026-03-31

# Action structure (n_missionaries_on_boat, n_cannibals_on_boat)
possible_actions = [(0,1), (1,0), (2,0), (0,2), (1,1)] # l'azione è la tupla (nrdimissionaridatrasportare, nrdicannibalidatrasportare)

# State structure (n_missionaries_on_left_side, n_cannibals_on_left_side, boat_position)

class MissionariesAndCannibalsProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.possible_actions = possible_actions

    def actions(self, state):
        actions = []
        for a in self.possible_actions:
            # check if the boat on the right side
            if state[2] == 1:
                # check if the boat passengers number is coherent with the number of missionaries and cannibals on the side where the boat is
                if state[1] >= a[1] and state[0] >= a[0]:
                    if ((3-state[0]+a[0])>=(3-state[1]+a[1]) or (3-state[0]+a[0]==0)) and ((state[0]-a[0])>=(state[1]-a[1]) or (state[0]-a[0]==0)): #ma il numero dei missionari a sx dopo il trasporto dovrà essere almeno pari a quello dei cannibali, oppure a sx non devono esserci missionari, e la stessa cosa a destra
                        actions.append(a)
            # check if the boat on the left side
            if state[2] == 0:
                # check if the boat passengers number is coherent with the number of missionaries and cannibals on the side where the boat is
                if (3-state[1]) >= a[1] and (3-state[0]) >= a[0]: #stessa cosa ma se la barca è a sx
                    if ((state[0]+a[0])>=(state[1]+a[1]) or (state[0]+a[0]==0)) and ((3-state[0]-a[0])>=(3-state[1]-a[1]) or (3-state[0]-a[0]==0)):
                        actions.append(a)
        return actions

    def result(self, state, action):
        state = list(state)
        # if the booat is on the right side
        if state[2] == 1: #se la barca è a dx, trasporterà verso sx e andrà a sx
            state[0] = state[0] - action[0]
            state[1] = state[1] - action[1]
            state[2] = 0
        # if the booat is on the left side
        elif state[2] == 0:
            state[0] = state[0] + action[0]
            state[1] = state[1] + action[1]
            state[2] = 1
        return tuple(state)

    def action_cost(self, state, action):
        return 1

    def is_goal(self, state):
        return state == self.goal_state
