import numpy as np

def read_matrix_from_file(filename):
    """Чтение матрицы из файла."""
    with open(filename, 'r') as f:
        matrix = []
        for line in f:
            # Преобразуем строку в список чисел
            row = list(map(int, line.split()))
            matrix.append(row)
    return np.array(matrix)

def write_matrix_to_file(matrix, filename):
    """Запись матрицы в файл."""
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

def sort_columns_by_kth_row(matrix, k):
    """Сортировка столбцов матрицы по k-й строке."""
    if k < 1 or k > len(matrix):
        raise ValueError("k должно быть в пределах от 1 до M (количество строк матрицы).")
    
    k_index = k - 1
    sorted_indices = np.argsort(matrix[k_index])
    sorted_matrix = matrix[:, sorted_indices]
    
    return sorted_matrix

# Основная часть программы
input_file = 'ФИО_группа_vvod.txt'
output_file = 'ФИО_группа_vivod.txt'
k = 2  # Указываем номер строки для сортировки (например, 2 для второй строки)

# Читаем матрицу из файла
matrix = read_matrix_from_file(input_file)

# Сортируем столбцы матрицы по k-й строке
try:
    sorted_matrix = sort_columns_by_kth_row(matrix, k)
    # Записываем отсортированную матрицу в файл
    write_matrix_to_file(sorted_matrix, output_file)
    print("Сортировка выполнена и результаты записаны в файл.")
except ValueError as e:
    print(e)