# Global variables
vertices = ['A', 'B', 'C', 'D', 'E']  # List of vertices in the graph
vertices_no = len(vertices)  # Number of vertices in the graph
graph = [
    [0, 10, 0, 60, 7],  # A
    [10, 0, 20, 0, 0],  # B
    [0, 20, 0, 32, 0],  # C
    [60, 0, 32, 0, 0],  # D
    [7, 0, 0, 0, 0]     # E
]  # Adjacency matrix representing the graph

# Print the graph with header and formatted output
def print_graph():
    global vertices
    global graph

    # Print the header
    print("Vertices =", vertices)
    print("Edges:")

    # Print the edges
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], "->", vertices[j], "edge weight:", graph[i][j])

# Call the print_graph function
print_graph()
