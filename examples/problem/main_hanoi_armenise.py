from problems.hanoiTower.armenise import HanoiProblem
from path_search.node import *
from path_search.strategies import *
from path_search.search import Search

problem = HanoiProblem(((3,2,1),(),()), ((),(),(3,2,1)))

print("possible actions are", problem.actions(((3,2,1),(),()))) #prima verifica

search_istance= Search(problem, BreadthFirstStrategy())
final_node = search_istance.run()

if final_node != None:
    print(f"La soluzione è stata trovata. Essa è: {final_node.path()}")
    print(f"il costo per la soluzione vale {final_node.path_cost}")
else:
    print ("non è stata trovata soluzione")