import sys

def dijkstra(matrix, start_vertex):
    """
    Функция реализует алгоритм Дейкстры для поиска кратчайших путей
    от начальной вершины до всех остальных в графе, заданном матрицей смежности.
    """
    num_vertices = len(matrix)
    
    # Шаг 1: Инициализация массивов
    # Расстояния до всех вершин изначально принимаем за бесконечность
    distances = [sys.maxsize] * num_vertices
    # Расстояние до начальной вершины всегда равно 0
    distances[start_vertex] = 0
    
    # Массив для отслеживания посещенных вершин
    visited = [False] * num_vertices

    # Шаг 2: Основной цикл алгоритма
    for _ in range(num_vertices):
        # Поиск вершины с минимальным расстоянием из еще не посещенных
        min_distance = sys.maxsize
        current_vertex = -1
        
        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                current_vertex = v
                
        # Если мы не нашли доступных вершин, завершаем работу
        if current_vertex == -1:
            break
            
        # Отмечаем текущую вершину как посещенную
        visited[current_vertex] = True
        
        # Шаг 3: Обновление расстояний до соседей
        for neighbor in range(num_vertices):
            # Проверяем, есть ли ребро (вес > 0) и не посещен ли сосед
            if matrix[current_vertex][neighbor] > 0 and not visited[neighbor]:
                new_distance = distances[current_vertex] + matrix[current_vertex][neighbor]
                # Если нашли путь короче — обновляем его
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    
    return distances


if __name__ == "__main__":
    # Пример графа в виде матрицы смежности (5 вершин: 0, 1, 2, 3, 4)
    # Число — это расстояние. 0 — дороги нет.
    graph_matrix = [
        [0, 4, 2, 0, 0],  # Соседи вершины 0
        [4, 0, 1, 5, 0],  # Соседи вершины 1
        [2, 1, 0, 8, 10], # Соседи вершины 2
        [0, 5, 8, 0, 2],  # Соседи вершины 3
        [0, 0, 10, 2, 0]  # Соседи вершины 4
    ]
    
    start = 0
    print(f"--- Расчёт кратчайших путей от вершины {start} ---")
    
    results = dijkstra(graph_matrix, start)
    
    # Красивый вывод результатов
    for vertex, distance in enumerate(results):
        if distance == sys.maxsize:
            print(f"До вершины {vertex}: путь отсутствует")
        else:
            print(f"До вершины {vertex}: минимальное расстояние равно {distance}")