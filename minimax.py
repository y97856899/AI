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


def minimax(node, depth, maximizing, children, evaluate):
    if depth == 0 or not children(node):  # Base case: max depth or no moves
        return evaluate(node)
    if maximizing:
        return max(minimax(child, depth - 1, False, children, evaluate) for child in children(node))
    else:
        return min(minimax(child, depth - 1, True, children, evaluate) for child in children(node))

# Example problem setup (generic without positions)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

# Children function
def children(node):
    return graph.get(node, [])

# Example heuristic (simply count the depth of the node or something specific to your problem)
def simple_heuristic(node):
    return ord(node) - ord('A')  # A simple heuristic: alphabetic order difference

# Run minimax with the generic heuristic
best_score = minimax('A', 3, True, children, simple_heuristic)
print("Best Score:", best_score)