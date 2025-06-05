import numpy as np

class MinCostFlowSolver:
    """Реализация алгоритма Беллмана-Форда для потока минимальной стоимости."""

    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes
        self.graph = np.zeros((num_nodes, num_nodes), dtype=float)
        self.capacity = np.zeros((num_nodes, num_nodes), dtype=float)
        self.cost = np.zeros((num_nodes, num_nodes), dtype=float)
        self.flow = np.zeros((num_nodes, num_nodes), dtype=float)

    def add_edge(self, u: int, v: int, capacity: float, cost: float):
        """Добавляет ребро u → v с пропускной способностью и стоимостью."""
        self.graph[u][v] = 1
        self.capacity[u][v] = capacity
        self.cost[u][v] = cost

    def solve(self, source: int, sink: int) -> tuple[float, float]:
        """Возвращает (максимальный поток, минимальную стоимость)."""
        max_flow = 0
        min_cost = 0

        while True:
            # Алгоритм Беллмана-Форда для поиска пути
            distance = [float('inf')] * self.num_nodes
            parent = [-1] * self.num_nodes
            distance[source] = 0

            for _ in range(self.num_nodes - 1):
                updated = False
                for u in range(self.num_nodes):
                    for v in range(self.num_nodes):
                        if (self.graph[u][v] and
                            self.capacity[u][v] > self.flow[u][v] and
                            distance[u] + self.cost[u][v] < distance[v]):
                            distance[v] = distance[u] + self.cost[u][v]
                            parent[v] = u
                            updated = True
                if not updated:
                    break

            if parent[sink] == -1:
                break  # Пути больше нет

            # Находим минимальный остаточный поток
            path_flow = float('inf')
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v] - self.flow[u][v])
                v = u

            # Обновляем поток
            v = sink
            while v != source:
                u = parent[v]
                self.flow[u][v] += path_flow
                self.flow[v][u] -= path_flow
                min_cost += path_flow * self.cost[u][v]
                v = u

            max_flow += path_flow

        return max_flow, min_cost