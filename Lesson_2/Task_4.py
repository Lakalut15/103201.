"""
Задание 4 Калькулятор

Создать скрипт, который просит ввести ввести число, операцию и снова число и выводит на экран ответ.
Скрипт должен поддерживать стандартные арифметические операции операции: +, -, /, *,
на остальные операции выдать сообщение об ошибке. Обратите внимание, что на 0 делить нельзя,
потому продумайте эту ситуацию.

Примечание! Пользоваться циклами запрещено.

Пример:
-Введите первое число:
>> 1
-Введите операцию:
>>+
-Введите второе число:
>> 2
- Ответ: 3


Пример 2:
-Введите первое число:
>> 1
-Введите операцию:
>>/
-Введите второе число:
>> 0
- Ошибка! На 0 делить нельзя

"""
print('Введите число')
a = int(input())
print('Введите операцию')
b = input()
if b != '*' and b != '+' and b != '-' and b != '/':
    print('Введите корректную информацию')
    b = input()

print('Введите второе число')
c = int(input())
if b == '*':
    print("Ответ:" + str(a*c))

if b == '/' and c == 0:
    print('На ноль делить нельзя! Введите корректное число')
    c = int(input())
    print("Ответ:" + str(a / c))
elif b == '/':
    print("Ответ:" + str(a / c))

if b == '+':
    print("Ответ:" + str(a + c))

if b == '-':
    print("Ответ:" + str(a - c))

