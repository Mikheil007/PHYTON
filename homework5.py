# Задание 5 Реализуйте алгоритм перемешивания списка.

n = int(input("Введите количество элементов в списке: "))
import random
firstlist = [random.randint(1, 100) for i in range(n+1)]
print(firstlist)
random.shuffle(firstlist)
print(firstlist)
