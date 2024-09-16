# Recursive DFS implementation
def DFS(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)

# Main code
if __name__ == "__main__":
    # Input number of nodes and edges
    nodes = int(input("Enter the number of nodes: "))
    edges = int(input("Enter the number of edges: "))
    
    # Initialize the graph as a dictionary
    graph = {i: [] for i in range(nodes)}
    
    # Input the edges
    print("Enter the edges (node1 node2):")
    for _ in range(edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # Assuming undirected graph
    
    # Input the starting node
    start_node = int(input("Enter the starting node: "))
    
    # Call DFS
    print("DFS Traversal starting from node", start_node, ":")
    visited = set()
    DFS(graph, start_node, visited)
