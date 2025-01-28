def count_numbers_with_digits(a, b, c, N):
    count = 0
    # Генерируем все трехзначные числа от 100 до N
    for number in range(100, N + 1):
        # Преобразуем число в строку и получаем его цифры
        digits = set(str(number))
        # Проверяем, состоят ли все цифры числа из a, b, c
        if digits.issubset({str(1), str(2), str(3)}):
            count += 1
    return count

# Пример использования
a = 1 
b = 2  
c = 3 
N = 230

result = count_numbers_with_digits(a, b, c, N)
print(f"Количество чисел на отрезке [100, {N}] из цифр {a}, {b}, {c}: {result}")








def reverse_words_in_string(input_string):
    # Разбиваем строку на слова
    words = input_string.split()
    # Изменяем порядок слов на обратный
    reversed_words = words[::-1]
    # Соединяем слова обратно в строку
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Пример использования
input_string = "Привет мир это тестовая строка"
result = reverse_words_in_string(input_string)
print("Исходная строка:", input_string)
print("Обратная последовательность слов:", result)