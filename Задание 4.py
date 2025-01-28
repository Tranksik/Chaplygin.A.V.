def print_numbers_in_range():
    # Считываем два целых числа
    A = 3
    B = 7
    
    # Проверяем условие A ≤ B
    if A > B:
        print("Ошибка: A должно быть меньше или равно B.")
        return
    
    # Выводим числа от A до B включительно
    for number in range(A, B + 1):
        print(number)

# Вызов функции
print_numbers_in_range()