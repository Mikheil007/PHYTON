
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# num = int(input('enter number'))
# if num == 6 or num == 7:
#     print('weekend')
# elif num < 1 or num > 7:
#     print('you entered the wrong day of the week')
# elif num > 1 and num < 6:
#     print('not weekend')


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# def logical_statement(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)
# if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and
# logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
# logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")


# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# x = int(input("Введите координату X: "))
# y = int(input("Введите координату Y: "))
#
# if x == 0 or y == 0:
#     print("Одна или несколько координат находится в нулевой зоне")
# else:
#     if   x > 0 and y > 0: print("Вы попали в 1 четверть оси координат!")
#     elif x < 0 and y > 0: print("Вы попали в 2 четверть оси координат!")
#     elif x < 0 and y < 0: print("Вы попали в 3 четверть оси координат!")
#     else:                 print("Вы попали в 4 четверть оси координат!")












