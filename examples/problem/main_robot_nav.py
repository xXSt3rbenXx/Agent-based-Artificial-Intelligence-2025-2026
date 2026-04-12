# from problems.robotNavigation.Squeo import RobotNavigationProblem, Position
from problems.robotNavigation.v1 import RobotNavigationProblem
from path_search.search import Search
from path_search.strategies import RandomStrategy, UniformCostStrategy

rows = 3
columns = 3
# # Initial State
# initial_position = Position(0, 0, None)
# # Goal State
# goal_position = Position(2, 2, None)


problem = RobotNavigationProblem((0,0), (2,2), rows, columns)

strategy = UniformCostStrategy()  

search = Search(problem, strategy)
result = search.run()

if result is not None:
    path = result.path()
    state = problem.initial_state
    for action in path:
        print(f'[{state}] --{action}--> ', end='')
        state = problem.result(state, action)
    print(f'[{state}]')
    print(f'Path cost: {result.path_cost}')
