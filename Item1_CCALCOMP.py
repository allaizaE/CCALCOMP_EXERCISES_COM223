# Global variables
graph = []  # Adjacency matrix representing the graph
vertices_no = 0  # Number of vertices in the graph
vertices = []  # List of vertices in the graph

# Main function
def main():
    add_vertex('A')
    add_vertex('B')
    add_vertex('C')
    add_vertex('D')
    add_vertex('E')

    add_edge('A', 'B', 10)
    add_edge('B', 'C', 20)
    add_edge('C', 'A', 12)
    add_edge('C', 'D', 32)
    add_edge('A', 'D', 60)
    add_edge('A', 'E', 7)

    print_graph()

# Add a vertex to the set of vertices and the graph
def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if v in vertices:
        print("Vertex ", v, " already exists")
    else:
        vertices_no = vertices_no + 1
        vertices.append(v)
        if vertices_no > 1:
            for vertex in graph:
                vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

# Print the graph
def print_graph():
    global graph
    global vertices_no

    # Print the header
    print("Vertices =", vertices)
    print("Edges:")
    
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], " -> ", vertices[j],
                      " edge weight: ", graph[i][j])

# Call the main function if this script is run directly
if __name__ == "__main__":
    main()
