# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

N = int(input("Введите число N: "))
a = int(input("Введите номер первого числа: "))
b = int(input("Введите номер второго числа: "))

from random import randint
numbers = [randint(-N, N) for i in range(-N, N + 1)]
print(numbers)
result = numbers[a-1] * numbers[b-1]
print("Произведение элементов: ", result)
