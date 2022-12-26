# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

print("Введите число: ")
n = int(input())

list = []
list1 = []
fib1 = 1
fib2 = 0
fib3 = 1
fib4 = 0
i = 0
while(n + 1 > i):
	fib1, fib2 = fib2, fib1 - fib2
	list.append(fib1)
	fib3, fib4 = fib4, fib3 + fib4
	list1.append(fib3)
	i = i + 1

list.reverse()
print(list + list1[1:])