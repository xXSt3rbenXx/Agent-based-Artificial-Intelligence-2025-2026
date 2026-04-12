# Author: Armenise Roberta
# Date: 2026-04-11


class HanoiProblem:
    def __init__(self,initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self,state):
        peg0, peg1, peg2 = state
        pegs = [peg0, peg1, peg2]

        valid_actions = []
        #(i,j) da pegi sposta a pegj

        for i in range(3):
            for j in range(3):
                if i != j:
                    if len(pegs[i]) > 0:
                        if len(pegs[j]) == 0 or pegs[j][-1] > pegs[i][-1]:
                            valid_actions.append((i,j))

        return valid_actions

    def result(self, state, action):
        peg0, peg1, peg2 = state
        pegs = [peg0, peg1, peg2] #rendo la tupla lista per lavorarci

        i, j = action

        disk = pegs[i][-1]  #memorizzo quale disco voglio spostare

        pegs[i] = pegs[i][:-1]  #se tolgo quel disco da quel peg, come deve diventare il peg?
        pegs[j] = pegs[j] + (disk,) # al peg di destinazione aggiungo il disco che ho memorizzato

        return tuple(pegs) #restituisco la lista pegs sottoforma di tupla

    def action_cost(self, state, action):
        return 1

    def is_goal(self,state):
        return state == self.goal_state

