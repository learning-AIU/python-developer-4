from collections.abc import Callable, Sequence



def simple_separator() -> str:
    """Функция возвращает красивый разделитель из 10-и звездочек (**********)

    :return: **********
    """



def long_separator(count: int) -> str:
    """Функция возвращает разделитель из звездочек число которых можно регулировать параметром count

    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """



def separator(symbol: str, count: int) -> str:
    """Функция возвращает разделитель из любых символов любого количества

    :param symbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """



def hello_world() -> None:
    """Функция выводит в stdout Hello World в формате:

    **********

    Hello World!

    ##########
    """



def hello_who(who: str = 'World') -> None:
    """Функция выводит в stdout приветствие в красивом формате

    **********

    Hello {who}!

    ##########

    :param who: кого мы приветствуем (World по умолчанию)
    """



def pow_many(power: int, *numbers: int) -> int:
    """Функция складывает любое количество чисел и возводит результат в степень power

    :param power: степень
    :param numbers: произвольное количество чисел
    :return: результат вычисления
    """



def print_key_val(**kwargs) -> None:
    """Функция выводит переданные параметры в виде key --> value, где: key - имя параметра, value - значение параметра

    :param kwargs: любое количество именованных параметров
    """



# усложнённое задание
def my_filter(iterable: Sequence, function: Callable) -> list:
    """Функция фильтрует последовательность iterable и возвращает новую: если function от элемента последовательности возвращает True, то элемент входит в новую последовательность, иначе нет

    :param iterable: входная последовательность
    :param function: функция фильтрации (предикат)
    :return: новая отфильтрованная последовательность
    """



print(simple_separator() == '**********')
# True

print(long_separator(3) == '***')
# True
print(long_separator(4) == '****')
# True

print(separator('-', 10) == '----------')
# True
print(separator('#', 5) == '#####')
# True

hello_world()
# **********
#
# Hello World!
#
# ##########

hello_who()
# **********
#
# Hello World!
#
# ##########
hello_who('Max')
# **********
#
# Hello Max!
#
# ##########
hello_who('Kate')
# **********
#
# Hello Kate!
#
# ##########

print(pow_many(1, 1, 2) == 3)
# True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)
# True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)
# True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)
# True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)
# True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

print_key_val(name='Max', age=21)
# name --> Max
# age --> 21
print_key_val(animal='Cat', is_animal=True)
# animal --> Cat
# is_animal --> True

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])
# True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])
# True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])
# True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])
# True
