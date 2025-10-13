# MAP COLORING PROBLEM USING BACKTRACKING

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

def is_safe(node, color, coloring):
    for neighbor in graph[node]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def map_coloring(node_list, coloring):
    if not node_list:
        return coloring
    
    node = node_list[0]
    for color in colors:
        if is_safe(node, color, coloring):
            coloring[node] = color
            result = map_coloring(node_list[1:], coloring)
            if result:
                return result
            del coloring[node]
    
    return None

nodes = list(graph.keys())
solution = map_coloring(nodes, {})

print("Colors Map Coloring Solution:", solution)
