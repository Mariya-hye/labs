import networkx as nx

def analyze_random_graph():
    # 1. Параметры из задания
    n = 25  # Количество вершин
    p = 0.9  # Вероятность появления ребра
    
    print(f"--- Генерация случайного графа Эрдёша-Реньи (n={n}, p={p}) ---")
    
    # 2. Генерация графа по модели Эрдёша-Реньи
    G = nx.erdos_renyi_graph(n, p)
    
    # 3. Расчет практической средней степени вершины
    total_degree = sum(dict(G.degree()).values())
    practical_average_degree = total_degree / n
    
    # 4. Расчет теоретической средней степени по формуле из лекций: (n - 1) * p
    theoretical_average_degree = (n - 1) * p
    
    # 5. Вывод результатов для сравнения
    print(f"Практическое среднее значение (из графа): {practical_average_degree:.4f}")
    print(f"Теоретическое значение (по формуле):    {theoretical_average_degree:.4f}")
    
    # Находим разницу (погрешность случайности)
    difference = abs(practical_average_degree - theoretical_average_degree)
    print(f"Разница из-за случайности генерации:    {difference:.4f}")

if __name__ == "__main__":
    analyze_random_graph()
