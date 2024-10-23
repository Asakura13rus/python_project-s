def apply_all_func(int_list, *functions):
    results = {}  # Создаем пустой словарь для результатов
    for func in functions:
        # Применяем каждую функцию и записываем результат в словарь
        results[func.__name__] = func(int_list)
    return results

# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))