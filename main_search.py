from problems.street_problem import StreetProblem
from cities import * 
from search import Search
from strategies import RandomStrategy

problem = StreetProblem(TRANI, MODUGNO)

strategy = RandomStrategy()
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
    
