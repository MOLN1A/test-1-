import math
 
OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b,
}
FUNCTIONS = {"sin": math.sin, "cos": math.cos, "tan": math.tan,
             "sqrt": math.sqrt, "log": math.log}
def evaluate_rpn(rpn):
    """Вычисляет значение выражения, заданного в обратной польской записи."""
    stack = []
    for token in rpn:
        if isinstance(token, float):
            stack.append(token)
        elif token in OPERATORS:
            if len(stack) < 2:
                raise ArithmeticError("недостаточно операндов")
            b = stack.pop()
            a = stack.pop()
            stack.append(OPERATORS[token](a, b))
        elif token in FUNCTIONS:
            if len(stack) < 1:
                raise ArithmeticError("недостаточно операндов")
            a = stack.pop()
            stack.append(FUNCTIONS[token](a))
        else:
            raise ArithmeticError(f"неизвестный токен: {token!r}")
    if len(stack) != 1:
        raise ArithmeticError("некорректное выражение")
    return stack[0]
