from problems.robotNavigation.armenise import GridProblem
from path_search.search import Search
from path_search.strategies import *
from path_search.node import Node

problem = GridProblem(
    3,
    3,
    { (1,1), (2,1)},
    (0,0),
    (2,2)
)

print("possible actions are" , problem.actions((0,0)))

search_istance = Search(problem, BreadthFirstStrategy() )
final_node = search_istance.run()

if final_node is not None:
    print(final_node.path())
    print(f'Il costo per raggiungere il goal è {final_node.path_cost}')
else:
    print("non è stata trovata una soluzione")
