from path_search.search import Search
from path_search.strategies import AStarStrategy

from problems.robotNavigation.v1 import RobotNavigationProblem

problem = RobotNavigationProblem(initial_state=(0,0), goal_state=(2,2), rows=3, columns=3)
strategy = AStarStrategy(problem=problem)
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is not None:
    path = result.path()
    state = problem.initial_state
    for action in path:
        print(f'[{state}] --go_to_{action}({problem.action_cost(state, action)})--> ', end='')
        state = problem.result(state, action)
    print(f'[{state}]')
    print(f'Path cost: {result.path_cost}')
    
