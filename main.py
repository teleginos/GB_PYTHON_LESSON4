import re
from collections import defaultdict
from random import randint


def creating_lists(a: int, flag: int, n: int = 0) -> list:
    list_number: list = []
    print(f"\nСоздаем массив № {n}")
    for i in range(a):
        if flag:
            list_number.append(int(input(f"Введите {i + 1} число: ")))
        else:
            list_number.append(randint(1, 10))
    return list_number


def case1():
    print("""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
           Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
           Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
           Затем пользователь вводит сами элементы множест.\n""")

    n: int = int(input("Введите кол-во элементов первого множества: "))
    m: int = int(input("Введите кол-во элементов второго множества: "))
    choice_flag: int = int(input("\nВыбор опции для создания массива:\n"
                                 "0 - если вы хотите что бы программа сама генерировала все массивы\n"
                                 "1 - если вы хотите вводить значения массива вручную\n"
                                 "Ваш выбор: "))

    list_number_1: list = creating_lists(n, choice_flag, n=1)
    print("=" * 50)
    list_number_2: list = creating_lists(m, choice_flag, n=2)
    print("=" * 50)

    print(f"Массив 1 = {list_number_1}\nМассив 2 = {list_number_2}")
    print(f"Отсортированный список чисел которые встречаются в обоих списках =  "
          f"{sorted(set(list_number_1) & set(list_number_2))}")


def case2():
    print("""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
          Она растёт на круглой грядке, причём кусты высажены только по окружности.
          Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
          Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число
          ягод — на i-ом кусте выросло a[i] ягод.В этом фермерском хозяйстве внедрена система автоматического сбора
          черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей
          Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
          собирает ягоды с этого куста и с двух соседних с ним.Напишите программу для нахождения максимального 
          числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом 
          заданной во входном списке урожайности грядки.\n""")

    def max_berrises(a: list) -> int:
        n = len(a)
        max_sum = 0
        for i in range(n):
            current_sum = a[i] + a[(i - 1) % n] + a[(i + 1) % n]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum

    number_of_bushes: int = int(input("Введите кол-во кустов на грядке: "))

    choice_flag: int = int(input("\nВыбор опции для создания массива:\n"
                                 "0 - если вы хотите что бы программа сама генерировала все массивы\n"
                                 "1 - если вы хотите вводить значения массива вручную\n"
                                 "Ваш выбор: "))

    crop_list: list = creating_lists(number_of_bushes, choice_flag, n=1)

    print(f"Список с урожаем со всех кустов = {crop_list}\nМаксимального числа ягод, которое может собрать за один "
          f"заход собирающий модуль = {max_berrises(crop_list)}")


def case3():
    def convert_to_base(num: int, base: int) -> str:
        conversion = "0123456789ABCDEF"
        result = ''
        while num > 0:
            num, remainder = divmod(num, base)
            result = conversion[remainder] + result
        return result if result else "0"

    number: int = int(input("Введите число для конвертации: "))
    choice_base: int = int(input("""Введите число для определения системы конвертации:
    2 - двоичная система
    3 - троичная система
    8 - восьмеричная система
    12 - двенадцатиричная система
    16 - шестнадцатиричная система
    Ваш выбор: """))

    print(f"Результат конвертации числа {number} в {choice_base} систему счисления ="
          f" {convert_to_base(number, choice_base)}")


def case4():
    import sympy as sp

    def add_polynomials(poly1, poly2):
        x = sp.symbols('x')  # Определить символ 'x'
        poly1 = poly1.replace("^", "**")  # Преобразовать степень в Python синтаксис
        poly2 = poly2.replace("^", "**")  # Преобразовать степень в Python синтаксис

        poly1 = sp.sympify(poly1)  # Преобразовать строку в sympy выражение
        poly2 = sp.sympify(poly2)  # Преобразовать строку в sympy выражение

        sum_poly = sp.expand(poly1 + poly2)  # Складываем полиномы и раскрываем скобки
        sum_poly = str(sum_poly).replace('**', '^')

        return sum_poly

    poly1 = "2*x^2 + 4*x + 5"
    poly2 = "5*x^3 - 3*x^2 - 12"
    print(add_polynomials(poly1, poly2))  # Выводит: 5.0*x^3 - x^2 + 4.0*x - 7.0


def default():
    print("\nВы выбрали неизвестный случай")


switch_case = {
    1: case1,
    2: case2,
    3: case3,
    4: case4
}

user_input: int = int(input("1: Задача про неупорядоченный набор целых чисел\n"
                            "2: Задача про кусты с черникой\n"
                            "3: Задача по конвертации числа в двоичную и восьмеричную систему\n"
                            "4: Задача про формирование многочленов\n\nВыберите номер задания для запуска кода: "))

print("=" * 50)
switch_case.get(user_input, default)()
