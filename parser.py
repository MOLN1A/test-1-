"""Парсер: лексический разбор выражения и перевод в обратную польскую запись."""
import math

# Библиотека математических функций (внешние подпрограммы модуля math)
FUNCTIONS = {
    'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
    'sqrt': math.sqrt, 'log': math.log10, 'ln': math.log, 'abs': math.fabs,
}

# Приоритеты операций: ^ выше, чем * и /, те выше, чем + и -
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
RIGHT_ASSOC = {'^'}


def tokenize(expression):
    """Разбивает строку на токены: числа, имена функций, операции, скобки."""
    tokens = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch.isspace():
            i += 1
        elif ch.isdigit() or ch == '.':
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            tokens.append(float(num))
        elif ch.isalpha():
            name = ''
            while i < len(expression) and expression[i].isalpha():
                name += expression[i]
                i += 1
            tokens.append(name)
        elif ch in '+-*/^%':
            tokens.append(ch)
            i += 1
        elif ch in '(),' :
            tokens.append(ch)
            i += 1
        else:
            raise ValueError(f'недопустимый символ {ch!r}')
    return tokens


def to_rpn(tokens):
    """Алгоритм сортировочной станции: токены -> ОПЗ.

    Унарный минус обозначается 'uneg' с высшим приоритетом.
    """
    output = []
    stack = []
    prev = None
    for tok in tokens:
        if isinstance(tok, float):
            output.append(tok)
        elif tok in FUNCTIONS:
            stack.append(tok)
        elif tok == ',':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
        elif tok in PRECEDENCE:
            if tok == '-' and (prev is None or prev in PRECEDENCE or prev in ('(', ',')):
                stack.append('uneg')          # унарный минус
            else:
                while (stack and stack[-1] in PRECEDENCE and
                       (PRECEDENCE[stack[-1]] > PRECEDENCE[tok] or
                        (PRECEDENCE[stack[-1]] == PRECEDENCE[tok] and tok not in RIGHT_ASSOC))):
                    output.append(stack.pop())
                stack.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError('несбалансированные скобки')
            stack.pop()
            if stack and stack[-1] in FUNCTIONS:
                output.append(stack.pop())    # функция без аргументов
        prev = tok
    while stack:
        if stack[-1] in ('(', ')'):
            raise ValueError('несбалансированные скобки')
        output.append(stack.pop())
    return output
