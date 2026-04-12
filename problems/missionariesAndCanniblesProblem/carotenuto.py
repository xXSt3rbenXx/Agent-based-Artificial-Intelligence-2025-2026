# Author: Carotenuto Giusy
# Date: 2026-04-10


C1= 'muovi un cannibale'
C2= 'muovi 2 cannibali'
M1= 'muovi un missionario'
M2= 'muovi 2 missionari'
M1C1= 'muovi un cannibale ed un missionario'

class MissionariesAndCannibalsProblem:

#un problema è definito dallo state-space, stato iniziale, goal condition (o sets), azioni e model transition
    def __init__(self, initial_state, goal_state):

        self.initial_state= initial_state
        self.goal_state= goal_state

        self.map= {
            C1: (+1, 0, +1), #ipotizzo barca a destra (1) e mantengo la sponda destra. In questo modo se sposto un cannibale faccio -1 e tengo traccia che a destra vi è un cannibale in meno
            C2: (+2, 0, +1),
            M1: (0, +1, +1),
            M2: (0, +2, +1),
            M1C1: (+1, +1, +1),
        }

    def actions(self, state):
        azioni_possibili = []
        for i in self.map:
            c_right, m_right, barca= state
            c, m, b= self.map[i]
            if barca == 0:
                new_mr=  m_right + m
                new_cr = c_right + c
                new_ml= 3- new_mr
                new_cl = 3 - new_cr
                if 0 <= new_cr <= 3 and 0 <= new_mr <= 3 and 0 <= new_cl <= 3 and 0 <= new_ml <= 3:
                    ok_destra = (new_mr >= new_cr or new_mr == 0)
                    ok_sinistra = (new_ml >= new_cl or new_ml == 0)
                    if ok_destra and ok_sinistra:
                        azioni_possibili.append(i)
            else:
                new_mr=  m_right - m
                new_cr = c_right - c
                new_ml= 3- new_mr
                new_cl = 3 - new_cr
                if 0 <= new_cr <= 3 and 0 <= new_mr <= 3 and 0 <= new_cl <= 3 and 0 <= new_ml <= 3:

                    ok_destra = (new_mr >= new_cr or new_mr == 0)
                    ok_sinistra = (new_ml >= new_cl or new_ml == 0)

                    if ok_destra and ok_sinistra:
                        azioni_possibili.append(i)
        return azioni_possibili


    def result(self, state, action):
        c_right, m_right, barca = state
        c, m, b = self.map[action]

        if barca == 0:
            new_mr = m_right + m
            new_cr = c_right + c
            new_ml = 3 - new_mr
            new_cl = 3 - new_cr
            if 0 <= new_cr <= 3 and 0 <= new_mr <= 3 and 0 <= new_cl <= 3 and 0 <= new_ml <= 3:
                ok_destra = (new_mr >= new_cr or new_mr == 0)
                ok_sinistra = (new_ml >= new_cl or new_ml == 0)
                if ok_destra and ok_sinistra:
                    return (new_cr, new_mr, barca+b)
        else:
            new_mr = m_right - m
            new_cr = c_right - c
            new_ml = 3 - new_mr
            new_cl = 3 - new_cr
            if 0 <= new_cr <= 3 and 0 <= new_mr <= 3 and 0 <= new_cl <= 3 and 0 <= new_ml <= 3:

                ok_destra = (new_mr >= new_cr or new_mr == 0)
                ok_sinistra = (new_ml >= new_cl or new_ml == 0)

                if ok_destra and ok_sinistra:
                    return (new_cr, new_mr, barca - b)

        return state

    def is_goal(self, state):
        return state==self.goal_state

    def action_cost(self, state, action):
        return 1

