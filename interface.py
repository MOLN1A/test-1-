"""Подсистема интерфейса: ввод выражения и вывод результата."""


def input_expression():
    """Ввод арифметического выражения пользователем."""
    return input('Введите выражение (команды: history - журнал, exit - выход): ')


def output_result(expression, result):
    """Вывод результата вычисления на экран."""
    print(f'{expression} = {result}')
