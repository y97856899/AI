# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:31:13 2024

@author: Hp
"""

file = open("C:/Users/Hp/Desktop/Yousuf/systematic.txt.txt","r")

start=file.readline().strip()
#start= file1[0].strip()
goal= file.readline().strip()
graph={}
#count=0
while True:
    contant = file.readline().rstrip()
    if(contant==""):
        break
#    count+=1
    #contant.rstrip()
    contant = contant.replace(":",";").split(";")
    #contant = contant.split(";")
#    if(contant[-1]==''):
#        contant.pop()
    key=contant[0].strip()
    val = []
    for i in range(1,len(contant)):
        if contant[i]:
            node,cost = map(int,contant[i].split(","))
            val.append((str(node),cost))
#        strr = tuple(map(int,val[i].split(",")))
#        name,cost=strr
#        name=str(name)
#        addit=(cost,str(name))
#        val[i]=addit
        graph[key] = val
        
#    if (len(contant)==1):
#        val=[]
#        graph[key]=val
#    else:
#        graph[key]=val
    
print(graph)

def dfs(graph, start,goal):
    visited=[]
    stack = [[start]]
    while stack:
        path=stack.pop()
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjcent_nodes = graph.get(node,[])
            for node2 in adjcent_nodes:
                new_path = path+[node2]
#                new_path = path.copy()
#                new_path.append(node2[1])
                stack.append(new_path)
                
                
                
                
                
def bfs(graph, start,goal):
    visited=[]
    queue = [[start]]
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjcent_nodes = graph.get(node,[])
            for node2 in adjcent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                queue.append(new_path)            
                
                
                
def path_cost(path):
    totalCost = 0
    for(node,cost)in path:
        totalCost+=cost
        return totalCost,path[-1][0]
                
                
                
              
def ucs(graph, start,goal):
    visited=[]
    queue = [[start,0]]
    while queue:
        queue.sort(key=path_cost)
        path=queue.pop()
        node=path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node==goal:
            return path
        else:
            adjcent_nodes = graph.get(node,[])
            for (node2,cost) in adjcent_nodes:
                new_path = path.copy()
                new_path.append(node2,cost)
                queue .append(new_path) 
                
                
                
option = (input("Select which search algorithm to apply from the following list:\n"
      "1. Depth-first search\n"
      "2. Breadth-first search\n"
      "3. Uniform cost search\n"
      "Enter the number only: "))                
                

if option == "1":
    result = dfs(graph, start, goal)
    if result:
        print("DFS Path:", result)
    else:
        print("No path found with DFS.")

elif option == "2":
    result = bfs(graph, start, goal)
    if result:
        print("BFS Path:", result)
    else:
        print("No path found with BFS.")

elif option == "3":
    result = ucs(graph, start, goal)
    if result:
        path, cost = result
        print("UCS Path:", [node for node, _ in path])
        print("UCS Path Cost:", cost)
    else:
        print("No path found with UCS.")
else:
    print("Wrong input")
    
   
                
file.close()                