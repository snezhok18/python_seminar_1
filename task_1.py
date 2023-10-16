# Задача 2: Найдите сумму цифр трехзначного числа.

number = 154
number = str(number)
sum = 0
for i in range(len(number)):
    sum += int(number[i])

print(sum)