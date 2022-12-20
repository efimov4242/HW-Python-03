# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI

def get_some_list(lenght = 5, min_value = 1, max_value = 9):
	list = [RI(min_value, max_value) for i in range(lenght)]
	return list

def get_sum_odd_elements(list):
	sum = 0
	for i in range(0, len(list), 2):
		sum += list[i]
	return sum

new_list = get_some_list()

print(new_list)
print(get_sum_odd_elements(new_list))