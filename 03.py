# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.3, 3.1, 5.0, 10.025]

right_elements = []

for i in list:
	right = i - int(i)
	right = round(right, 2)
	if right > 0: right_elements.append(right)


print(right_elements)


print(round(max(right_elements) - min(right_elements), 2))

