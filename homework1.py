# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

num = int(input('enter number'))
if num == 6 or num == 7:
    print('weekend')
elif num < 1 or num > 7:
    print('you entered the wrong day of the week')
elif num > 1 and num < 6:
    print('not weekend')



