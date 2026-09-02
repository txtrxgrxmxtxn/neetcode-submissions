class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        #Construir grafo como lista de adyacencia
        graph = defaultdict(list)
        for u, v, w in times: 
            graph[u].append((v,w)) #(nodo destino, tiempo)

        #Dijkstra algoritmo
        distances = {node: float('inf') for node in range(1, n+1)}
        distances[k] = 0


        #min-heap: (tiempo acumulado, nodo)
        min_heap = [(0, k)]

        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)
            #Si encontramos un t. mayor que el registrado ignorar
            if current_time > distances[current_node]:
                continue

            #explorar vecinos
            for neighbor, travel_time in graph[current_node]:
                new_time = current_time + travel_time 


                #Si encontramos ruta mas corta
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        #Encontrar la dist. máxima
        max_time = max(distances.values())

        #Si algun nodo es inalcanzable
        return max_time if max_time != float('inf') else -1 
        