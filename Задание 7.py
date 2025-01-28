def find_duplicates_in_list():
    # Считываем список чисел (или любых элементов)
    elements = input("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1").split()
    
    # Преобразуем элементы в множество для нахождения дубликатов
    seen = set("1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1")
    duplicates = set("1")
    
    for element in elements:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)
    
    # Проверяем наличие дубликатов и выводим результат
    if duplicates:
        print("Повторяющиеся элементы:", " ".join(duplicates))
    else:
        print("Повторяющиеся элементы отсутствуют.")

# Вызов функции
find_duplicates_in_list()







import random

def transform_array():
    # Создаем массив из 15 случайных элементов от 0 до 30
    original_array = [random.randint(0, 30) for _ in range(15)]
    
    # Преобразуем массив
    transformed_array = []
    for value in original_array:
        if value < 10:
            transformed_array.append(0)  # Присваиваем 0, если элемент меньше 10
        elif value > 20:
            transformed_array.append(1)  # Присваиваем 1, если элемент больше 20
        else:
            transformed_array.append(value)  # Оставляем элемент без изменений

    # Выводим результаты
    print("Первоначальный массив:", original_array)
    print("Преобразованный массив:", transformed_array)

# Вызов функции
transform_array()