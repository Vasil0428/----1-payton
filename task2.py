# Задача 2: Найдите сумму цифр трехзначного числа.#
# *Пример:*#
# 123 -> 6 (1 + 2 + 3)# 100 -> 1 (1 + 0 + 0) |

number_one = int (input("Введите число :"))
sum = 0
for i in range(2):    
    divided_number = number_one % 10
    sum = sum + divided_number    
    number_one = number_one // 10
output = (number_one + sum)
print(output)