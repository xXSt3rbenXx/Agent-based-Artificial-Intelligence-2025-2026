# from problems.waterJug.Mastromauro import WaterJugProblem
# from problems.waterJug.v1 import WaterJugProblem
from problems.waterJug.v2 import WaterJugProblem
from path_search.search import Search
from path_search.strategies import RandomStrategy, UniformCostStrategy

problem = WaterJugProblem((8,0,0))

strategy = RandomStrategy()
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