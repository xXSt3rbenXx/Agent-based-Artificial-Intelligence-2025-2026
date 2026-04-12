# from problems.robotNavigation.Squeo import RobotNavigationProblem, Position
from problems.networkRouting.Squeo import *
from path_search.search import Search
from path_search.strategies import RandomStrategy, UniformCostStrategy

initial_state = A
goal_state = E

problem = NetworkRoutingProblem(initial_state, goal_state)
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
else:
    print("No solution found.")