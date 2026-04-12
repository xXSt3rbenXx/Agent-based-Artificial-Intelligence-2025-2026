
class HillClimbing:

    def __init__(self, problem) -> None:
        self.problem = problem

    def neighbours(self, state):
        states = []
        for action in self.problem.actions(state):
            states.append(self.problem.result(state, action))
        return states

    def run(self):
        state = self.problem.initial_state

        while True:
            # if self.problem.is_goal(state):
            #     return state
            utility = self.problem.evaluate(state)
            neighbours = self.neighbours(state)
            new_state = max(neighbours, key=lambda x: self.problem.evaluate(x))
            new_utility = self.problem.evaluate(new_state)
            if new_utility < utility:
                return state
            state = new_state

