# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("**Проверки истинности утверждения \n¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z\n для всех значений предикат**")
print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if (not (x or y or z)) == (not x and not y and not z):
                print(x, y, z, "-> True")
            else:
                print(x, y, z, "-> False")