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


def bfs1(graph,start,goal):
    visit = []
    queue = [[start]]
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visit:
            visit.append(node)
            
            if node==goal:
                return path
            
       
             
        adj = graph.get(node,[])
        for m in adj:
            path2 = path +[m]
            queue.append(path2)
       



print(bfs1(graph,(0,0),(2,3)))