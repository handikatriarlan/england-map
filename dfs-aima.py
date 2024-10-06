from aima.search import GraphProblem, UndirectedGraph, depth_first_tree_search

romania_map = UndirectedGraph(dict(
    Manchester = dict(Liverpool=None, Sheffield=None),
    Liverpool = dict(Manchester=None, Shrewsbury=None),
    Sheffield = dict(Manchester=None, Nottingham=None),
    Shrewsbury = dict(Liverpool=None, Aberystwyth=None, Birmingham=None),
    Nottingham = dict(Sheffield=None, Oxford=None, Birmingham=None),
    Aberystwyth = dict(Shrewsbury=None, Cardiff=None),
    Birmingham = dict(Shrewsbury=None, Nottingham=None, Bristol=None),
    Cardiff = dict(Aberystwyth=None, Bristol=None),
    Bristol = dict(Birmingham=None, Cardiff=None, Southampton=None),
    Oxford = dict(Nottingham=None),
    Southampton = dict(Bristol=None),
))

start_city = input("Input your starting city: ").strip().title()
goal_city = input("Input your destination city: ").strip().title()

romania_problem = GraphProblem(start_city, goal_city, romania_map)

result = depth_first_tree_search(romania_problem)

if result:
    solution_path = result.solution()
    
    if solution_path and solution_path[0] != start_city:
        solution_path.insert(0, start_city)
    
    solution_string = ' -> '.join(solution_path)
    
    print("Solution path from", start_city, "to", goal_city, ":", solution_string)
else:
    print("No solution found from", start_city, "to", goal_city)
