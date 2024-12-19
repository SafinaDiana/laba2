import random

def find_multiples():
    try:
        x = int(input("Введите число X: "))
        if x <= 0:
            print("Ошибка: X должно быть положительным числом.")
            return

        numbers = [random.randint(0, 200) for _ in range(10)]

        multiples = list(filter(lambda num: num % x == 0, numbers))

        print(f"Список случайных чисел: {numbers}")
        print(f"Числа, кратные {x}: {multiples}")
    except ValueError:
        print("Ошибка: Введите корректное число.")

find_multiples()