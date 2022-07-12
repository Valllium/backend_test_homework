from math import sqrt

message = ("Добро пожаловать в самую лучшую"
           "программу для вычисления квадратного"
           "корня из заданного числа.")


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    if number <= 0:
        return 0
    else:
        value = sqrt(number)
        return print("Мы вычислили корень квадратный"
                     f"из введенного вами числа. Это будет:{value}")


print(message)
calculate_square_root(25.5)
