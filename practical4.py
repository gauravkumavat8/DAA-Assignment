import sys  # For handling large integer values

# Function to find the vertex with the minimum key value from the set of vertices not yet included in MST
def min_key(key, mst_set, V):
    min_val = sys.maxsize  # Initialize the minimum value
    min_index = -1
    
    # Loop over all vertices to find the minimum key value
    for v in range(V):
        if key[v] < min_val and mst_set[v] == False:
            min_val = key[v]
            min_index = v
            
    return min_index

# Function to print the constructed MST stored in parent[]
def print_mst(parent, graph, V):
    print("Edge \tWeight")
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

# Function to construct and print MST for a graph represented using adjacency matrix representation
def prim_mst(graph, V):
    # Array to store constructed MST
    parent = [None] * V
    
    # Key values used to pick minimum weight edge in cut
    key = [sys.maxsize] * V
    
    # To represent set of vertices included in MST
    mst_set = [False] * V
    
    # Always include the first vertex in MST
    key[0] = 0  # Make key 0 so that this vertex is picked as the first vertex
    parent[0] = -1  # First node is always the root of MST
    
    for _ in range(V):
        # Pick the minimum key vertex from the set of vertices not yet included in MST
        u = min_key(key, mst_set, V)
        
        # Add the picked vertex to the MST set
        mst_set[u] = True
        
        # Update the key and parent index of the adjacent vertices of the picked vertex
        for v in range(V):
            # graph[u][v] is non zero only for adjacent vertices of u
            # mst_set[v] is False for vertices not yet included in MST
            # Update the key only if graph[u][v] is smaller than key[v]
            if graph[u][v] > 0 and mst_set[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u
    
    # Print the constructed MST
    print_mst(parent, graph, V)

# Example usage:
if __name__ == "__main__":
    # Number of vertices in the graph
    V = 5
    
    # Graph represented as an adjacency matrix
    graph = [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0]]
    
    # Function call
    prim_mst(graph, V)
