# Author: Armenise Roberta
# Date: 2026-04-11


class GridProblem:
    def __init__(self,rows,cols,obstacles,initial_state, goal_state):
        self.rows = rows
        self.cols = cols
        self.obstacles = obstacles
        self.initial_state = initial_state
        self.goal_state = goal_state

        #state lo rappresento come una tupla (x,y) con x row e y column

        #obstacles lo farò tipo un insieme di tuple {(x,y),(x',y'),(x'',y'')...}

    def actions (self, state):
        r, c = state
        valid_actions= []

        up = (r-1, c)
        down = (r+1, c)
        left = (r, c-1)
        right = (r, c+1)

        if 0 <= up[0] < self.rows and 0 <= up[1] < self.cols and up not in self.obstacles:
            valid_actions.append("up")

        if 0 <= down[0] < self.rows and 0 <= down[1] < self.cols and down not in self.obstacles:
            valid_actions.append("down")

        if 0 <= left[0] < self.rows and 0 <= left[1] < self.cols and left not in self.obstacles:
            valid_actions.append("left")

        if 0 <= right[0] < self.rows and 0 <= right[1] < self.cols and right not in self.obstacles:
            valid_actions.append("right")

        return valid_actions

    def result (self, state, action):
        r, c = state

        if action == "up":
            return (r-1, c)
        elif action == "down":
            return (r+1, c)
        elif action == "left":
            return (r, c-1)
        elif action == "right":
            return (r, c+1)

    def action_cost(self, state, action):
        return 1

    def is_goal (self, state):
        return state == self.goal_state


