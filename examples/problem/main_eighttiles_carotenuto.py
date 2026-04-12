from path_search.search import Search
from path_search.strategies import *
from problems.eightTiles.carotenuto import EightTiles

problem= EightTiles(initial_state= ((3,5,6),(1,2,7),(8,0,4)), goal_state=((1,2,3),(4,5,6),(7,8,0)))
search= Search(problem, BreadthFirstStrategy())

result= search.run()

if result is None: print('soluzione non trovata')
else:
    print(f'{result.state}, {result.depth}')
    print(f'{result.path()}')

