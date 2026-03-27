from node import Node
from problems.street_problem import StreetProblem

def expand(node, problem):
    actions = problem.actions(node.state)
    new_nodes = []
    for action in actions:
        new_state = problem.result(node.state, action)
        new_node = Node(state=new_state, action=action, parent=node, path_cost=node.path_cost+problem.action_cost(node.state, action))    
        new_nodes.append(new_node)
    return new_nodes

class Search:

    def __init__(self, problem, strategy) -> None:
        
        self.problem: StreetProblem = problem
        self.strategy = strategy

    def run(self):
        print()
        root_node = Node(state=self.problem.initial_state, action=None, parent=None, path_cost=0)
        fringe = [root_node]
        visited = []

        while len(fringe) > 0:
            
            fringe, node = self.strategy.select(fringe)

            if self.problem.is_goal(node.state):
                return node

            new_nodes = expand(node, self.problem)
            fringe = fringe + new_nodes
        
        return None


