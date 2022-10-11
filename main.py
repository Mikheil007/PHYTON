
# 6) Капитан Америка и Халк бьются против Таноса и Сёрфера.
#   Узнай, у какой команды удар сильнее, если удар Капитана Америки - k, Халка - h
#   А сила ударов во второй команде - У Таноса - t, Сёрфера - s
#   Сила ударов вводится с клавиатуры.
#   Вывести нужно у какой команды урон сильнее

# k = int(input('enter power CA'))
# h = int(input('enter power HK'))
# t = int(input('enter power TS'))
# s = int(input('enter power SR'))
# # kh = k + h
# # ts = t + s
# if k + h > t + s:
#     print(f'team 1 - {k + h}')
# else:
#     print(f'team 2 - {t + s}')


# 4) Команда разработчиков набирает мальчиков
# от 10 до 15 лет включительно.
#   Напишите программу, которая запрашивает возраст
# и пол претендента, используя обозначение пола буквы
# м -  мужчина и ж - женщина. и говорим подходит ли претендент
# для вступления в команду или нет.
# Если претендент подходит, то выведите «Вы приняты»,
# иначе выведите «Вы не тот кто нужен».

# age = int(input('enter age boys'))
# sex = input('enter male or female')
# if (age > 9 and age < 16) and (sex == 'male'):
#     print('you child has joined')
# else:
#     print('you child do not joined')

# Необходимо вбивать с клавиатуры слова до тех пор,
# пока слово не будет равно YES
#
# word = input('enter word')
# while word != 'yes':
#     print(word)
#     word = input('enter word')

# 2) Усложняем и YES или yes

# word = input('enter word')
# while word != 'YES' and word != 'yes':
#     print(word)
#     word = input('enter word')

# # 3) Вводим с клавиатуры числа, делящиеся на 3.
# # Программа будет работать до тех пор, пока не введем число,
# # не делящее на 3
#
# num = int(input('enter number'))
# while num % 3 == 0:
#     print(num)
#     num = int(input('enter number'))

# 4) Вбиваем с клавиатуры целое число N,
# а затем выводим на экран все числа от 1 до N

n = int(input('enter number'))
while n > 1:
      print (n + 1)
      n = int(input('enter number'))




























