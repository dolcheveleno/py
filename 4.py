# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quart_coord = int(input("Введите номер четверти от 1 до 4: "))

if   quart_coord == 1: print("Первая четверть имеет диапозон точек: x от 0 до +бесконечности и y от 0 до +бесконечности") 
elif quart_coord == 2: print("Вторая четверть имеет диапозон точек: x от 0 до -бесконечности и y от 0 до +бесконечности")  
elif quart_coord == 3: print("Третья четверть имеет диапозон точек: x от 0 до -бесконечности и y от 0 -бесконечности")
elif quart_coord == 4: print("Четвертая четверть имеет диапозон точек: x от 0 до +бесконечности и y от 0 до -бесконечности")
else:        print("Неверно задано значение, повторите попытку!")