""" Урок 1 - 1. Типы данных и операции присваивания"""

"""
Присвоение переменных
Присвоение осуществляется с помощью оператора =.

"""

# Например:
a=1
print(a) # 1

# Множественное присвоение
a=b=3
print(a) #3
print(b) #3

# Операция распаковки:
a,b=5,6
print(a) #5
print(b) #6




"""
Типы данных и преобразование типов
Перечислим основные типы данных в Python, 
которые понадобятся на ближайших уроках:

int – целочисленные значения;
float – вещественные (дробные) значения;
bool – логические значения — истина (True) или ложь (False);
str – символьная строка или единичный символ.

"""

# Целые числа(int):

num = 13
print(num)  # 13

num = 0
print(num)  # 0

num = -10
print(num)  # -10

# Вещественные числа(float):

num = 0.0
print(num)  # 0.0

num = -15.2
print(num)  # -15.2

num = 100000.000002
print(num)  # 100000.000002

num = 1.7e2  # 1.7 умножить на 10 в степени 2
print(num)  # 170

# Логический тип(bool):

print(15 == 15)  # True
print(1 != 3)  # True
print(3 > 4)  # False
print(3 <= 3)  # True
print(6 >= 6)  # True
print(6 < 5)  # False
x = 2
print(1 < x < 3)  # True

# Строки(str):

example_string = "Очень интересно"
print(example_string)  # Очень интересно

example_string = 'Пьеса "На дне"'
print(example_string)  # Пьеса "На дне"

example_string = "Пьеса \"На дне"
print(example_string)  # Пьеса "На дне"

example_string = "Как " \
                 "разбить " \
                 "объявление длинной строки"
print(example_string)  # Как разбить объявление длинной строки

example_string = """
                 Как  
                 оставить сроку
                 в несколько строк
                 """
print(example_string)
# Как
# оставить сроку
# в несколько строк
# Как объединить две строки в одну

print("Можно их" + " сложить")  # Можно их сложить

print("Можно и так!" * 3)  # Можно и так!Можно и так!Можно и так!


# Тип данных можно определить с помощью функции type()
a="Строка"
print(type(a)) # <class 'str'>
b=10.5
print(type(b)) # <class 'float'>

# Преобразование в символьную строку:
a = 1.7
a=str(a)
print(a) # '1.7'

# преобразование в целое число:

x = 1.7
x=int(x)
print(x) # 1
# Обратите внимание, что преобразование дробного
# числа в тип int просто отбрасывает дробную часть, а не округляет число

# преобразование в вещественное:

y=1
y=float(y)
print(y) # 1.0


"""
Перевод в другие системы исчисления
bin(y) — целое число преобразовывается в двоичную строку.
hex(y) — целое число преобразовывается в шестнадцатеричную строку.
oct(y) — целое число преобразовывается в восьмеричную строку.
"""

print(bin(17)) # '0b10001'
print(oct(17)) # '0o21'
print(hex(17)) # '0x11'