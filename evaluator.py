"""Вычислитель: вычисление значения выражения по ОПЗ стековым алгоритмом."""
import math
from parser import tokenize, to_rpn, FUNCTIONS


def evaluate(expression):
    """Полный конвейер вычислений: строка -> токены -> ОПЗ -> результат."""
    tokens = tokenize(expression)
    rpn = to_rpn(tokens)
    stack = []
    for token in rpn:
        if isinstance(token, float):
            stack.append(token)
        elif token == 'uneg':
            stack.append(-stack.pop())
        elif token in FUNCTIONS:
            stack.append(FUNCTIONS[token](stack.pop()))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '%':
                stack.append(a % b)
            elif token == '^':
                stack.append(a ** b)
    if len(stack) != 1:
        raise ValueError('ошибка вычисления')
    return stack[0]
