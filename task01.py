# Задайте список из нескольких чисел. Напишите программу, к
# оторая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI

n = int(input("Введите количество элементов в списке: "))

my_list = [RI(0,10) for i in range(n)]
print(my_list)    

index_list =[my_list for i in range(len(my_list)) if i%2 != 0]

sum = 0
for i in index_list:
    sum += my_list[i]

print(f'Сумма нечетеых элементов равна {sum}.') 