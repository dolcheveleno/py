# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def DayRecognition(dayNumber):
 if dayNumber == 6 or dayNumber == 7:
    print("This day is day off!")
 elif dayNumber > 0 and dayNumber < 6:
    print("This day is work day!")
 elif dayNumber < 1 or dayNumber > 7:
    print("You entered wrong number. Try again!")

print("Please enter some day number and I'll try to recognize that it is a day off or a working day.")
dayNumber = int(input("Inter day number: "))
DayRecognition(dayNumber)