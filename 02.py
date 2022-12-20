# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]

def get_mult_couples_elements(list):
	mult = 0
	for i in range(len(int(list)/2), 1):
		mult[i] = list[i] * list[len(list) - i - 1]
	return mult

print(get_mult_couples_elements(list))