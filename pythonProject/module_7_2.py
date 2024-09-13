def custom_write(file_name, strings):
    # Открываем файл на запись с указанием кодировки utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}  # Словарь для хранения номеров строк и байтовых позиций
        for i, string in enumerate(strings, start=1):
            # Получаем текущую позицию в файле перед записью строки
            position = file.tell()
            # Записываем строку с добавлением символа новой строки
            file.write(string + '\n')
            # Заполняем словарь: (номер строки, байт начала строки) -> строка
            strings_positions[(i, position)] = string
    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

# Вызов функции и вывод результата
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)