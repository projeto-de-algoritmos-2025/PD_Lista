class Solution(object): 
    def findCheapestPrice(self, n, flights, src, dst, k):
        
        INF = float('inf')
        # Inicializa distâncias com infinito, exceto a origem
        dist = [INF] * n
        dist[src] = 0

        # Executa Bellman-Ford por no máximo k+1 vezes (k paradas = k+1 voos)
        for _ in range(k + 1):
            # Usar uma cópia para evitar atualizações simultâneas na mesma rodada
            temp = dist[:]
            for u, v, cost in flights:
                if dist[u] != INF:
                    temp[v] = min(temp[v], dist[u] + cost)
            dist = temp

        return -1 if dist[dst] == INF else dist[dst]
