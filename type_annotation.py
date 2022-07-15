from typing import Callable

def add(number: float, callback: Callable[[float], float]) -> float:
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    """    
    return callback(number)


def adder20(number):
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number):
    """Умножает аргумент на 2."""
    return number * 2

add(20,adder20(10))
