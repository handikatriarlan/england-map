from aima.search import GraphProblem, UndirectedGraph, greedy_best_first_graph_search

romania_map = UndirectedGraph(dict(
    Manchester = dict(Liverpool=30, Sheffield=40),
    Liverpool = dict(Manchester=30, Shrewsbury=70, Nottingham=110),
    Sheffield = dict(Manchester=40, Nottingham=40),
    Shrewsbury = dict(Liverpool=70, Aberystwyth=80, Birmingham=50, Cardiff=110),
    Nottingham = dict(Sheffield=40, Oxford=100, Birmingham=50, Liverpool=110),
    Aberystwyth = dict(Shrewsbury=80, Cardiff=120),
    Birmingham = dict(Shrewsbury=50, Nottingham=50, Bristol=90, Oxford=70),
    Cardiff = dict(Aberystwyth=120, Bristol=50, Shrewsbury=110),
    Bristol = dict(Birmingham=90, Cardiff=50, Southampton=80),
    Oxford = dict(Nottingham=100, Birmingham=70, Southampton=70),
    Southampton = dict(Bristol=80, Oxford=70),
))

heuristic = {
    'Manchester': 180,
    'Liverpool': 200,
    'Sheffield': 160,
    'Shrewsbury': 120,
    'Nottingham': 140,
    'Birmingham': 100,
    'Aberystwyth': 220,
    'Cardiff': 130,
    'Bristol': 80,
    'Southampton': 0,
    'Oxford': 70
}

romania_map.locations = heuristic

class RomaniaProblem(GraphProblem):
    def h(self, node):
        return romania_map.locations[node.state]

start_city = input("Input your starting city: ").strip().title()
goal_city = input("Input your destination city: ").strip().title()

romania_problem = RomaniaProblem(start_city, goal_city, romania_map)

result = greedy_best_first_graph_search(romania_problem, lambda node: romania_problem.h(node))

if result:
    solution_path = result.solution()
    
    if solution_path and solution_path[0] != start_city:
        solution_path.insert(0, start_city)
    
    solution_string = ' -> '.join(solution_path)
    
    print("Solution path from", start_city, "to", goal_city, ":", solution_string)
else:
    print("No solution found from", start_city, "to", goal_city)
