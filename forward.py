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








def forward(graph, node, goal, path):
    path.append(node)
    if node == goal:
        return path
    
    # Perform forward checking: Check if there are valid moves for remaining nodes
    for n in graph.get(node, []):
        if n not in path:
            # Forward checking: Ensure there is at least one valid neighbor for future nodes
            if any(neighbor not in path for neighbor in graph.get(n, [])):
                result = forward(graph, n, goal, path)
                if result:
                    return result

    path.pop()
    return None

print(forward(graph, (0,0), (2,3), []))

   




def forward(graph,node,goal,path):
    path.append(node)
    if node==goal:
        return path
    for i in graph.get(node,[]):
        if i not in path:
            if any(n not in path for n in graph.get(i,[])):
                result = forward(graph,i,goal,path)
                if result:
                    return result
    path.pop()
    return None