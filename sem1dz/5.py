#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x=int(input('значение x -> '))
y=int(input('значение y -> '))
z=int(input('значение z -> '))
q=not(x or y or z) == ((not x) and (not y) and (not z))
print(q)