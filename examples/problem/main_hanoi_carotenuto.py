from path_search.search import Search
from path_search.strategies import *
from problems.hanoiTower.carotenuto import HanoiTowerProblem

pro= HanoiTowerProblem(([3,1], [2], []), ([], [], [3,2,1]))
search= Search(pro, DepthLimitedStrategy(limit=10))
result= search.run()

if result is None: print('soluzione non trovata')
else:
    print(f'{result.path()}')
    print(f'{result.path_cost}')