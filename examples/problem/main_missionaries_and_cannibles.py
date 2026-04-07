from problems.missionariesAndCanniblesProblem.v2 import MissionariesAndCannibalsProblem
from search import Search
from strategies import RandomStrategy, UniformCostStrategy

problem = MissionariesAndCannibalsProblem((3,3,1), (0,0,0))

strategy = UniformCostStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is not None:
    path = result.path()
    state = problem.initial_state
    for action in path:
        print(f'[{state}] --{action}--> ', end='')
        state = problem.result(state, action)
    print(f'[{state}]')
    print(f'Path cost: {result.path_cost}')
    
