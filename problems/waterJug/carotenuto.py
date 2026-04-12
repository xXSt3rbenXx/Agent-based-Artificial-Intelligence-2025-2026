# Author: Carotenuto Giusy
# Date: 2026-04-10


Riempi1= 'Riempi 1'
Riempi2= 'Riempi 2'
Riempi3= 'Riempi 3'
Svuota1= 'Svuota 1'
Svuota2= 'Svuota 2'
Svuota3= 'Svuota 3'
Riempi12= 'Riempi 1 da 2'
Riempi13= 'Riempi 1 da 3'
Riempi23= 'Riempi 2 da 3'
Riempi21= 'Riempi 2 da 1'
Riempi31= 'Riempi 3 da 1'
Riempi32= 'Riempi 3 da 2'

class WaterJugProblem:

    def __init__(self, initial_state, goal_state):
        self.goal_state= goal_state
        self.initial_state = initial_state


    def actions(self, state):
        primo, secondo, terzo = state
        azioni= []

        if primo !=8:
            azioni.append(Riempi1)
            if secondo !=0:
                azioni.append(Riempi12)
            if terzo !=0:
                azioni.append(Riempi13)

        if secondo != 5:
            azioni.append(Riempi2)
            if primo !=0:
                azioni.append(Riempi21)
            if terzo !=0:
                azioni.append(Riempi23)

        if terzo != 3:
            azioni.append(Riempi3)
            if secondo !=0:
                azioni.append(Riempi32)
            if primo !=0:
                azioni.append(Riempi31)

        if primo != 0:
            azioni.append(Svuota1)

        if secondo != 0:
            azioni.append(Svuota2)

        if terzo != 0:
            azioni.append(Svuota3)

        return azioni

    def result(self, state, action):
        primo, secondo, terzo = state

        if primo != 8:
            if action==Riempi1:
                while primo<8:
                    primo+=1
            if secondo != 0 and action==Riempi12:
                while primo < 8 and secondo>0:
                    primo += 1
                    secondo -= 1
            if terzo != 0 and action==Riempi13:
                while primo < 8 and terzo > 0:
                    primo += 1
                    terzo -= 1

        if secondo != 5:
            if action==Riempi2:
                while secondo < 5:
                    secondo += 1
            if primo != 0 and action==Riempi21:
                while secondo < 5 and primo > 0:
                    primo -= 1
                    secondo += 1
            if terzo != 0 and action==Riempi23:
                while secondo<5 and terzo > 0:
                    secondo += 1
                    terzo -= 1

        if terzo != 3:
            if action==Riempi3:
                while terzo < 3:
                    terzo += 1
            if primo!= 0 and action==Riempi31:
                    while terzo < 3 and primo > 0:
                        primo -= 1
                        terzo += 1
            if secondo != 0 and action == Riempi32:
                while terzo<3 and secondo > 0:
                    secondo -= 1
                    terzo += 1

        if primo != 0 and action == Svuota1:
            while primo > 0:
                primo -= 1

        if secondo != 0 and action == Svuota2:
                while secondo > 0:
                    secondo -= 1

        if terzo != 0 and action == Svuota3:
                while terzo > 0:
                    terzo -= 1

        return (primo, secondo, terzo)


    def is_goal(self, state):
        primo, secondo, terzo= state
        if primo == self.goal_state or  secondo== self.goal_state or  terzo == self.goal_state:
            return True
        else:
            return False
        
    def action_cost(self, state, action):
        return 1
