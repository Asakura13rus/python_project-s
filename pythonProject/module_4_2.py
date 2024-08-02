def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()
    return 0


test_function()
# если вызвать функцию inner_function() выведет ошибку:
# NameError: name 'inner_function' is not defined.Did you mean: 'test_function'?
