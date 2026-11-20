"""Область данных «Журнал вычислений»: хранение истории вычислений."""


def create_journal():
    """Создаёт пустой журнал вычислений."""
    return []


def add_record(journal, expression, result):
    """Сохраняет в журнал пару: выражение и его результат."""
    journal.append((expression, result))


def show_history(journal):
    """Выводит историю вычислений на экран."""
    if not journal:
        print('Журнал вычислений пуст.')
        return
    print('--- Журнал вычислений ---')
    for n, (expression, result) in enumerate(journal, start=1):
        print(f'{n}. {expression} = {result}')
    print('-------------------------')
