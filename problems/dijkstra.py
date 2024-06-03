import heapq

def dijkstra(graph, start):

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 4},
    'C': {'A': 3, 'B': 2, 'D': 7},
    'D': {'B': 4, 'C': 7}
}
start_node = 'A'
result=dijkstra(graph,start_node)
print(result)