import random 

def Generate_Grid(N):
    grid=[[0 for m in range (N) ]for i in range(N)]
    
    O = round (((N * N) / 2 ) - 4)
    
    while O > 0:
        x, y = random.randint(0, N-1), random.randint(0, N-1)
        if grid[x][y] == 0:
            
            grid[x][y] = 1
            O -= 1
            
            
    
    while True:
        playerPos = (random.randint(0, N-1), random.randint(0, N-1))
        
        if grid[playerPos[0]][playerPos[1]] == 0:
            grid[playerPos[0]][playerPos[1]] = "P"
            
            break
    
    
    
    while True:
        npcPos = (random.randint(0, N-1), random.randint(0, N-1))
        if grid[npcPos[0]][npcPos[1]] == 0:
            grid[npcPos[0]][npcPos[1]] = "N"
            
            break

    return grid, playerPos, npcPos        
    


 



def Manhattan(x,y):
    man = abs(x[0]-y[0])+abs(x[1]-y[1])
    return man







def sort(pQueue):
    
    for i in range(len(pQueue) - 1):
        for j in range(len(pQueue) - i - 1):
            
            if pQueue[j][0] > pQueue[j + 1][0]:
                
                pQueue[j], pQueue[j + 1] = pQueue[j + 1], pQueue[j]
                
    return pQueue


moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]



def GBFS(grid, start, goal):
    
    
    pQueue = [(Manhattan(start, goal), start)]
    
    
    visited = set()
    visited.add(start)
    
    
    came = {start: None}
    


    while pQueue:
        
        pQueue = sort(pQueue)
        a, curr = pQueue.pop(0)
        
        
        if curr == goal:
            path = []
            while curr:
                path.append(curr)
                curr = came[curr]
            
            return path
        
        
        for mov in moves:
            
            adjecent = (curr[0] + mov[0], curr[1] + mov[1])
            
           
            if 0 <= adjecent[0] < len(grid) and 0 <= adjecent[1] < len(grid[0]) and grid[adjecent[0]][adjecent[1]] != 1:
                
                if adjecent not in visited:
                    
                    visited.add(adjecent)
                    came[adjecent] = curr
                    
                    pQueue.append((Manhattan(adjecent, goal), adjecent))
    
    return None  








def aStar(grid, start, goal):
   
    
    list1 = [(0 + Manhattan(start, goal), 0, start)]
    
   
    visited = set()
    cost = {start: 0}
    came = {start: None}
    
    

    while list1:
        
        list1 = sort(list1)
        
        
        entry = list1.pop(0)
        current = entry[2]
        
        
        if current == goal:
            path = []
            while current:
                
                path.append(current)
                current = came[current]
                
            path.reverse()
            
            return path
        
        visited.add(current)
        
        
        for mov in moves:
            adjecent = (current[0] + mov[0], current[1] + mov[1])
            
            
            if 0 <= adjecent[0] < len(grid) and 0 <= adjecent[1] < len(grid[0]) and grid[adjecent[0]][adjecent[1]] != 1:
                
                newCost = cost[current] + 1  #  cost of 1
                
                
                if adjecent not in cost or newCost < cost[adjecent]:
                    
                    cost[adjecent] = newCost
                    
                    fScore = newCost + Manhattan(adjecent, goal)
                    
                    list1.append((fScore, newCost, adjecent))
                    came[adjecent] = current
                    
    
    return None  




grid, playerPos, npcPos = Generate_Grid(10)
greedy = GBFS(grid, playerPos, npcPos)
aStar = aStar (grid, npcPos, playerPos)



for row in grid:
    print(row)
    

print("\nNPC position: ", npcPos)
print("player position: ", playerPos,"\n")

print("NPC's path to player cordinates for greedy best first search: ")
if greedy:
    for row in greedy:
        print(row)
else:
    print("Player is unreachable! ")

print("")


print("NPC's path to player cordinates for A*: ")
if aStar:
    for row in aStar:
        print(row)
else:
    print("Player is unreachable!")







