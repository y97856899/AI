graph = {
    #action ordering : PA , PB , FA , FB , EA , EB
    (0,0):{(4,0), (0,3)},
    (0,1):{(1,0),(4,1),(0,0)},
    (0,2):{(2,0),(4,2),(0,0)},
    (0,3):{(3,0),(4,3),(0,0),},
    (1,0):{(0,1),(1,3),(0,0)},
    (1,3):{(4,0),(0,3),(1,0)},
    (2,0):{(0,2),(2,3),(0,0)},
    (2,3):{(4,1),(0,3),(2,0)},
    (3,0):{(0,3),(3,3),(0,0)},
    (3,3):{(4,2),(0,3),(3,0)},
    (4,0):{(1,3),(4,3),(0,0)},
    (4,1):{(2,3),(0,1),(4,0)},
    (4,2):{(3,3),(4,0),(0,2)},
    (4,3):{(0,3),(4,0)}
  }

def backtracking(graph, node, goal, path):
    path.append(node)
    if node == goal:
        return path
    for neighbor in graph.get(node, []):
        if neighbor not in path:  # Avoid cycles
            result = backtracking(graph, neighbor, goal, path)
            if result:
                return result
    path.pop()  # Backtrack
    return None



print("back",backtracking(graph, (0,0), (2,3),[]))
