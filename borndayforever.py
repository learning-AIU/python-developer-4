"""Ветвления с циклами."""

from datetime import datetime as dt
from sys import stderr
from typing import Literal


correct_date = dt(year=1799, month=6, day=6)

PROMPT1 = 'введите правильный год рождения Александра Сергеевича Пушкина цифрами > '
PROMPT2 = 'введите правильные день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > '

OK_MESSAGE = "Верно"

ERR_MESSAGES = {
    'FORMAT': "\t_ обнаружены некорректные символы _",
    'YEAR': "\t_ неверный год рождения _",
    'DAY_MONTH': "\t_ неверный день рождения _",
}


def print_error(error_type: Literal['FORMAT', 'YEAR', 'DAY_MONTH']) -> None:
    print(ERR_MESSAGES[error_type.upper()], file=stderr)


def get_year() -> str:
    while True:
        ans_year = input(PROMPT1)
        if ans_year.isdecimal():
            if int(ans_year) == correct_date.year:
                return ans_year
            else:
                print_error('YEAR')
        else:
            print_error('FORMAT')


def get_date(year: str) -> None:
    while True:
        try:
            ans_day_month = input(PROMPT2)
            ans_date = dt.strptime(f"{ans_day_month}.{year}", '%d.%m.%Y')
        except ValueError:
            print_error('FORMAT')
            continue

        if ans_date == correct_date:
            return
        else:
            print_error('DAY_MONTH')


if __name__ == '__main__':
    get_date(get_year())
    print(OK_MESSAGE)


# stdout & stderr:
# введите правильный год рождения Александра Сергеевича Пушкина цифрами > не помню
#         _ обнаружены некорректные символы _
# введите правильный год рождения Александра Сергеевича Пушкина цифрами > 1799
# введите правильные день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > шестое июня
#         _ обнаружены некорректные символы _
# введите правильные день и месяц рождения Александра Сергеевича Пушкина цифрами через точку > 6.6
# Верно
