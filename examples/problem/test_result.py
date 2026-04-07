from problems.streetProblem.v2 import *

def test_result():
    problem = StreetProblem(ANDRIA, CORATO)
    state = CORATO
    actions = problem.actions(state)
    for action in actions:
        print(action, ' -> ', problem.result(state, action))
    print('Test passed!')

test_result()