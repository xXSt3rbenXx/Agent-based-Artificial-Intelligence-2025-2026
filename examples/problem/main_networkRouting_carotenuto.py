from path_search.search import Search
from path_search.strategies import *
from problems.networkRouting.carotenuto import NetworkRoutingProblem, A, F

problem= NetworkRoutingProblem(initial_state=A, goal_state=F)
search= Search(problem, BreadthFirstStrategy())

result= search.run()

if result is None: print('soluzione non trovata')
else:
    print(f'{result.path()}')
    print(f'{result.path_cost}')