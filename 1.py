import networkx as nx

def calculate_eigenvector_centrality():
    # Шаг 1: Создаем пустой неориентированный граф
    G = nx.Graph()
    
    # Шаг 2: Вручную добавляем ребра для графа-звезды (4 узла)
    # Узел 0 — центральный, связан со всеми тремя остальными
    G.add_edges_from([
        (0, 1),
        (0, 2),
        (0, 3)
    ])
    
    print("--- Расчёт меры центральности в собственных векторах ---")
    
    # Шаг 3: Вычисляем центральность в собственных векторах с помощью NetworkX
    centrality = nx.eigenvector_centrality(G)
    
    # Шаг 4: Выводим результаты на экран
    for node, value in centrality.items():
        print(f"Узел {node}: центральность = {value:.4f}")

if __name__ == "__main__":
    calculate_eigenvector_centrality()