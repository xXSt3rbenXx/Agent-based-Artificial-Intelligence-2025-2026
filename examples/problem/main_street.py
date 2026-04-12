from problems.streetProblem.v1 import StreetProblem
from problems.streetProblem.cities import * 
from path_search.search import Search
from path_search.strategies import RandomStrategy, UniformCostStrategy

problem = StreetProblem(TRANI, MODUGNO)

strategy = UniformCostStrategy()
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
    
