# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from random import randint

lst = []
N = int(input("Введите количество символов в случайной последовательности: "))
for i in range(N):
    lst.append(randint(0, 10))
lst_unique = list(item for item in lst if lst.count(item) == 1)
lst_no_repeat = list(set(lst))
lst_with_repeat = list(set(lst_no_repeat).difference(set(lst_unique)))
print(f"Исходная последовательность: {lst}")
print(f"Cписок уникальных элементов исходной последовательности: {lst_unique}")
print(f"Cписок повторяющихся элементов из исходной последовательности: {lst_with_repeat}")
print(f"Cписок элементов исходной последовательности без дубликатов: {lst_no_repeat}")
