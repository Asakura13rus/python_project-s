def test_function():
    def inner_function():
        print('Я в области видимости test_function!!!')
        return

    inner_function()
    return inner_function


i = test_function()
i()
