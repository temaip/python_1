#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("Введите x - "))
y = int(input("Введите y - "))
if x > 0 and y > 0:
    print("число находится в 1 четверти")
if x < 0 and y > 0:
    print("число находится во 2 четверти")
if x < 0 and y < 0:
    print("число находится в 3 четверти")
if x > 0 and y < 0:
    print("число находится в 4 четверти")
