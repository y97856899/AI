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



def path1(path):
    g_cost = 0
    for i,cost in path:
        g_cost+=cost
    last_node = path[-1][0]
    h_cost = H_table[last_node]
    f_cost = h_cost+g_cost

    return f_cost ,last_node

def aster(graph,start,goal):
    visit = []
    queue = [[(start,0)]]
    while queue:
        queue.sort(key=path1)
        path = queue.pop(0)
        node = path[-1][0]
        if node not in visit:
            visit.append(node)
            if node ==goal:
                return path 
            
        for i,m in graph.get(node,[]):
            path2 = path.copy()
            path2.append((i,m))
            queue.append(path2)
            
    return None        