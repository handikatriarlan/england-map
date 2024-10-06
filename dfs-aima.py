from aima.search import GraphProblem, UndirectedGraph, depth_first_graph_search

england_map = UndirectedGraph(dict(
    Manchester = dict(Liverpool=None, Sheffield=None),
    Liverpool = dict(Manchester=None, Shrewsbury=None, Nottingham=None),
    Sheffield = dict(Manchester=None, Nottingham=None),
    Shrewsbury = dict(Liverpool=None, Aberystwyth=None, Birmingham=None, Cardiff=None),
    Nottingham = dict(Sheffield=None, Oxford=None, Birmingham=None, Liverpool=None),
    Aberystwyth = dict(Shrewsbury=None, Cardiff=None),
    Birmingham = dict(Shrewsbury=None, Nottingham=None, Bristol=None, Oxford=None),
    Cardiff = dict(Aberystwyth=None, Bristol=None, Shrewsbury=None),
    Bristol = dict(Birmingham=None, Cardiff=None, Southampton=None),
    Oxford = dict(Nottingham=None, Birmingham=None, Southampton=None),
    Southampton = dict(Bristol=None, Oxford=None),
))

start_city = input("Input your starting city: ").strip().title()
goal_city = input("Input your destination city: ").strip().title()

england_problem = GraphProblem(start_city, goal_city, england_map)

result = depth_first_graph_search(england_problem)

if result:
    solution_path = result.solution()
    
    if solution_path and solution_path[0] != start_city:
        solution_path.insert(0, start_city)
    
    solution_string = ' -> '.join(solution_path)
    
    print("Solution path from", start_city, "to", goal_city, ":", solution_string)
else:
    print("No solution found from", start_city, "to", goal_city)
