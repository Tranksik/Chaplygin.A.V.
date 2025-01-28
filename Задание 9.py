def is_sorted(row):
    # Проверка на возрастание
    if all(row[i] <= row[i + 1] for i in range(len(row) - 1)):
        return True
    # Проверка на убывание
    if all(row[i] >= row[i + 1] for i in range(len(row) - 1)):
        return True
    return False

def max_in_sorted_rows(matrix):
    max_value = None  # Инициализируем переменную для хранения максимального значения
    for row in matrix:
        if is_sorted(row):  # Проверяем, упорядочена ли строка
            row_max = max(row)  # Находим максимальный элемент в строке
            if max_value is None or row_max > max_value:
                max_value = row_max  # Обновляем максимальное значение

    return max_value

# Пример использования
matrix = [
    [1, 2, 3, 4],    # Упорядочена по возрастанию
    [4, 3, 2, 1],    # Упорядочена по убыванию
    [1, 3, 2, 4],    # Не упорядочена
    [5, 6, 7, 8]     # Упорядочена по возрастанию
]

result = max_in_sorted_rows(matrix)
if result is not None:
    print("Максимальный элемент среди упорядоченных строк:", result)
else:
    print("Нет упорядоченных строк в матрице.")












    import NymPi as np

def sort_columns_by_kth_row(matrix, k):
    # Проверяем, что k находится в допустимых пределах
    if k < 1 or k > len(matrix):
        raise ValueError("k должно быть в пределах от 1 до M (количество строк матрицы).")
    
    # Индекс строки в Python (0-индексация)
    k_index = k - 1
    
    # Сортируем индексы столбцов по значениям в k-й строке
    sorted_indices = np.argsort(matrix[k_index])
    
    # Создаем новую матрицу с отсортированными столбцами
    sorted_matrix = matrix[:, sorted_indices]
    
    return sorted_matrix

# Пример использования
D = np.array([[5, 3, 8],
              [1, 7, 2],
              [4, 6, 9]])

k = 2  # Указываем номер строки для сортировки

try:
    sorted_D = sort_columns_by_kth_row(D, k)
    print("Исходная матрица:\n", D)
    print(f"Матрица с отсортированными столбцами по {k}-й строке:\n", sorted_D)
except ValueError as e:
    print(e)