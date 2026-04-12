from path_search.search import Search
from path_search.strategies import *
from problems.vacuumCleaner.carotenuto import VacuumCleanerProblem

pro= VacuumCleanerProblem((1,1), goal_state= [], celle_sporche=[(0,1), (0,0)])
search= Search(pro, strategy=BreadthFirstStrategy())
risultato = search.run()
if risultato:
    print(risultato.path())
else:
    print("Nessuna soluzione trovata.")