def find_longest_path(graph: list) -> int:
    vertex_count = len(graph)

    
    topological_order = perform_topological_sort(graph)

    return compute_longest_path(graph, topological_order)


def perform_topological_sort(graph):
    vertex_count = len(graph)
    visited_vertices = [False] * vertex_count
    order_stack = []

    def depth_first_search(vertex):
        visited_vertices[vertex] = True
        for adjacent_vertex, edge_weight in graph[vertex]:
            if not visited_vertices[adjacent_vertex]:
                depth_first_search(adjacent_vertex)
        order_stack.append(vertex)

    for vertex in range(vertex_count):
        if not visited_vertices[vertex]:
            depth_first_search(vertex)

    order_stack.reverse()
    return order_stack


def compute_longest_path(graph, topological_order):
    vertex_count = len(graph)
    longest_distances = [-float('inf')] * vertex_count

    
    for vertex in topological_order:
        if longest_distances[vertex] == -float('inf'):
            longest_distances[vertex] = 0

    for u in topological_order:
        if longest_distances[u] != -float('inf'):
            for v, weight in graph[u]:
                if longest_distances[u] + weight > longest_distances[v]:
                    longest_distances[v] = longest_distances[u] + weight

    #
    return max(longest_distances)
