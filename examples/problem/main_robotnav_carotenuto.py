from path_search.search import Search
from path_search.strategies import *
from problems.robotNavigation.carotenuto import RobotNavigationProblem

problem= RobotNavigationProblem(initial_state= (1,1), goal_state=(2,2), ostacolo= [(1,2)])
search= Search(problem, BreadthFirstStrategy())

result= search.run()

if result is None: print('soluzione non trovata')
else:
    print(f'{result.path()}')

