# Author: Carotenuto Giusy
# Date: 2026-04-10


daunoadue= 'da uno a due'
daunoatre= 'da uno a tre'
dadueatre= 'da due a tre'
dadueauno= 'da due a uno'
datreauno= 'da tre a uno'
datreadue= 'da tre a due'


class HanoiTowerProblem:

    def __init__(self, initial_state, goal_state):
        uno, due, tre = tuple(initial_state)
        self.initial_state= (tuple(uno), tuple(due), tuple(tre))
        uno, due, tre = tuple(goal_state)
        goal_state = (tuple(uno), tuple(due), tuple(tre))
        self.goal_state= goal_state


    def actions(self, state):
        azioni_possibili= []
        uno, due, tre = tuple(state)
        uno, due, tre = list(uno), list(due), list(tre)
        if len(uno)!=0:
            if len(due)==0:
                azioni_possibili.append(daunoadue)
            else:
                if due[-1] > uno[-1]:
                    azioni_possibili.append(daunoadue)

        if len(uno)!=0:
            if len(tre)==0:
                azioni_possibili.append(daunoatre)
            else:
                if tre[-1] > uno[-1]:
                    azioni_possibili.append(daunoatre)

        if len(due)!=0:
            if len(uno)==0:
                azioni_possibili.append(dadueauno)
            else:
                if uno[-1] > due[-1]:
                    azioni_possibili.append(dadueauno)

        if len(due)!=0:
            if len(tre)==0:
                azioni_possibili.append(dadueatre)
            else:
                if tre[-1] > due[-1]:
                    azioni_possibili.append(dadueatre)

        if len(tre)!=0:
            if len(uno)==0:
                azioni_possibili.append(datreauno)
            else:
                if uno[-1] > tre[-1]:
                    azioni_possibili.append(datreauno)

        if len(tre)!=0:
            if len(due)==0:
                azioni_possibili.append(datreadue)
            else:
                if due[-1] > tre[-1]:
                    azioni_possibili.append(datreadue)

        return azioni_possibili

    def result(self, state,action):
        uno, due, tre = tuple(state)
        uno, due, tre= list(uno), list(due), list(tre)
        if (action==daunoadue) and len(uno) != 0:
            if len(due) == 0:
                due.append(uno.pop())
            else:
                if due[-1] > uno[-1]:
                    due.append(uno.pop())

        if (action==daunoatre) and len(uno) != 0:
            if len(tre) == 0:
                tre.append(uno.pop())
            else:
                if tre[-1] > uno[-1]:
                    tre.append(uno.pop())

        if (action==dadueatre) and len(due) != 0:
            if len(tre) == 0:
                tre.append(due.pop())
            else:
                if tre[-1] > due[-1]:
                    tre.append(due.pop())

        if (action == dadueauno) and len(due) != 0:
            if len(uno) == 0:
                uno.append(due.pop())
            else:
                if uno[-1] > due[-1]:
                    uno.append(due.pop())

        if (action == datreauno) and len(tre) != 0:
            if len(uno) == 0:
                uno.append(tre.pop())
            else:
                if uno[-1] > tre[-1]:
                    uno.append(tre.pop())

        if (action == datreadue) and len(tre) != 0:
            if len(due) == 0:
                due.append(tre.pop())
            else:
                if due[-1] > tre[-1]:
                    due.append(tre.pop())

        return (tuple(uno), tuple(due), tuple(tre))


    def is_goal(self,state):
        return (state==self.goal_state)

    def action_cost(self, state, action):
        return 1