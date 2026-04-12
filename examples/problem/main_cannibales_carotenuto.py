from path_search.search import Search
from path_search.strategies import *
from problems.missionariesAndCanniblesProblem.carotenuto import MissionariesAndCannibalsProblem

pro= MissionariesAndCannibalsProblem((0,0,0), goal_state= (3,3,1))
strategy = BreadthFirstStrategy()
search= Search(problem=pro, strategy=strategy)
result= search.run()

if result is None: print('soluzione non trovata')
else:
    print(f'{result.path()}')
    print(f'{result.path_cost}')