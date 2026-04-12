from path_search.search import Search
from path_search.strategies import *
from problems.waterJug.carotenuto import WaterJugProblem

prob= WaterJugProblem(initial_state= (3,5,2), goal_state=4)
search= Search(prob, BreadthFirstStrategy())

result= search.run()

if result is None: print('soluzione non trovata')
else:
    print(f'{result.state}, {result.depth}')
    print(f'{result.path()}')
