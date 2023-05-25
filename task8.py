# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

x, y, z = input().split()
width = int(x)
height = int(y)
count = int(z)
isCan = False

square = width * height

for i in range(square, 0, -width):
    if (i == count):
        isCan = True

for i in range(square, 0, -height):
    if (i == count):
        isCan = True

if (isCan):
    print("yes")
else: 
    print("no")