"""Главный модуль приложения «Калькулятор».

Организует цикл обработки выражений, координирует вызов подсистем
интерфейса, вычислений и области данных «Журнал вычислений».
"""
from parser import tokenize, to_rpn
from evaluator import evaluate
from journal import create_journal, add_record, show_history
from interface import input_expression, output_result


def main():
    journal = create_journal()
    print('Приложение «Калькулятор» (вариант 5). '
          'Поддерживаются + - * / % ^, скобки, функции sin, cos, tan, sqrt, log, ln, abs.')
    while True:
        expr = input_expression().strip()
        if expr == 'exit':
            print('Завершение работы.')
            break
        if expr == 'history':
            show_history(journal)
            continue
        if not expr:
            continue
        try:
            tokens = tokenize(expr)      # лексический разбор
            rpn = to_rpn(tokens)         # перевод в обратную польскую запись
            result = evaluate(expr)      # вычисление по стековому алгоритму
            add_record(journal, expr, result)
            output_result(expr, result)
        except Exception as e:
            print(f'Ошибка: {e}')


if __name__ == '__main__':
    main()
