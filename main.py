def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов внутренней функции


# Вызов тестовой функции
test_function()

# Попытка вызвать inner_function вне test_function
try:
    inner_function()  # Это вызовет ошибку, так как inner_function не доступна здесь
except NameError as e:
    print("Ошибка:", e)