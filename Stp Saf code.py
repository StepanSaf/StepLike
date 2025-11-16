import random

def local_search_independent_set(graph):
    """
    Алгоритм локального поиска для нахождения независимого множества
    """
    # Начинаем со случайного независимого множества
    vertices = list(graph.keys())
    current_set = set()
    
    # Случайно добавляем вершины, проверяя независимость
    for vertex in random.sample(vertices, len(vertices)):
        is_independent = True
        for neighbor in graph[vertex]:
            if neighbor in current_set:
                is_independent = False
                break
        
        if is_independent:
            current_set.add(vertex)
    
    print(f"Начальное случайное независимое множество: {sorted(current_set)}")
    print(f"Размер начального множества: {len(current_set)}")
    
    # Основная фаза локального поиска
    improved = True
    iterations = 0
    
    while improved:
        improved = False
        iterations += 1
        
        # Пытаемся добавить вершины, которые не смежны с текущим множеством
        for vertex in vertices:
            if vertex not in current_set:
                # Проверяем, что вершина не смежна ни с одной вершиной в текущем множестве
                can_add = True
                for neighbor in graph[vertex]:
                    if neighbor in current_set:
                        can_add = False
                        break
                
                if can_add:
                    current_set.add(vertex)
                    improved = True
                    print(f"Итерация {iterations}: Добавлена вершина {vertex}")
                    print(f"Текущее множество: {sorted(current_set)}")
                    break
    
    return current_set, iterations

def create_random_graph(num_vertices, edge_probability=0.3):
    """
    Создает случайный граф с заданным количеством вершин
    """
    graph = {}
    
    # Инициализируем вершины
    for i in range(1, num_vertices + 1):
        graph[i] = []
    
    # Добавляем случайные ребра
    for i in range(1, num_vertices + 1):
        for j in range(i + 1, num_vertices + 1):
            if random.random() < edge_probability:
                graph[i].append(j)
                graph[j].append(i)
    
    return graph

def print_graph_info(graph):
    """Выводит информацию о графе"""
    print("\nСтруктура графа (вершина -> соседи):")
    for vertex in sorted(graph.keys()):
        print(f"Вершина {vertex}: {sorted(graph[vertex])}")
    
    total_edges = sum(len(neighbors) for neighbors in graph.values()) // 2
    print(f"\nВсего вершин: {len(graph)}")
    print(f"Всего рёбер: {total_edges}")
    print("=" * 50)

def get_positive_integer(prompt):
    """Получает положительное целое число от пользователя"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Ошибка: введите положительное число!")
        except ValueError:
            print("Ошибка: введите целое число!")

def get_float(prompt, min_value=0.0, max_value=1.0):
    """Получает дробное число от пользователя"""
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Ошибка: введите число от {min_value} до {max_value}!")
        except ValueError:
            print("Ошибка: введите число!")

# Основная программа
if __name__ == "__main__":
    print("ЛОКАЛЬНЫЙ ПОИСК ДЛЯ ЗАДАЧИ О НЕЗАВИСИМОМ МНОЖЕСТВЕ")
    print("=" * 50)
    
    # Получаем входные данные от пользователя
    num_vertices = get_positive_integer("Введите количество вершин в графе: ")
    edge_prob = get_float("Введите вероятность соединения вершин (0.0-1.0): ", 0.0, 1.0)
    seed = input("Введите seed для случайных чисел (или нажмите Enter для случайного): ")
    
    if seed.strip():
        random.seed(int(seed))
    else:
        random.seed()
    
    # Создаем граф
    graph = create_random_graph(num_vertices, edge_prob)
    
    print(f"\nСГЕНЕРИРОВАН ГРАФ С {num_vertices} ВЕРШИНАМИ")
    print_graph_info(graph)
    
    # Запускаем локальный поиск
    print("ЗАПУСК ЛОКАЛЬНОГО ПОИСКА")
    independent_set, iterations = local_search_independent_set(graph)
    
    print("\n" + "=" * 50)
    print("ФИНАЛЬНЫЙ РЕЗУЛЬТАТ:")
    print(f"Найденное независимое множество: {sorted(independent_set)}")
    print(f"Размер независимого множества: {len(independent_set)}")
    print(f"Количество итераций улучшения: {iterations}")
    
    # Проверяем корректность результата
    print("\nПРОВЕРКА КОРРЕКТНОСТИ:")
    is_valid = True
    for vertex in independent_set:
        for neighbor in graph[vertex]:
            if neighbor in independent_set:
                is_valid = False
                print(f"ОШИБКА: Вершины {vertex} и {neighbor} смежны!")
                break
        if not is_valid:
            break
    
    if is_valid:
        print("✓ Независимое множество корректно - нет смежных вершин")
    
    # Анализ эффективности
    print(f"\nАНАЛИЗ ЭФФЕКТИВНОСТИ:")
    print(f"Размер найденного множества: {len(independent_set)} из {num_vertices} вершин")
    print(f"Процент покрытия: {len(independent_set)/num_vertices*100:.1f}%")

