calls = 0


# считает колличество вызовов
def count_calls():
    global calls
    calls += 1


# принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(a):
    count_calls()
    b = len(a)
    c = a.upper()
    d = a.lower()
    e = (b, c, d)
    return e


# #принимает два аргумента: строку и список, и возвращает True,


# # если строка находится в этом списке,
# # False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(a, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() == a.lower():
            is_True = True
        else:
            is_True = False

    return is_True


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
