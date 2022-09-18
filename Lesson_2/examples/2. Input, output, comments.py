""" Урок 1 - 2. Input, output и комментарии"""

"""
Ввод данных
Ввод данных осуществляется через встроенную функцию input(message), 
которая возвращает строку. Вместо message можно ввести  сообщение пользователю.
Так же можно сразу присвоить введенные данные переменной

"""

# Пример:
msg=input('Введите сообщение:')


"""
Вывод данных
Вывод значения на экран осуществляется с помощью функции
print(value, ..., sep='', end='\n')

sep — это может быть строка, которую необходимо вставлять между 
значениями, по умолчанию — пробел.

end — это строка, которая добавляется после последнего значения. 
По умолчанию это перенос на новую строку (\n). 
С помощью аргумента end программист может самостоятельно определить 
окончание выражения print.
"""

# Пример

string='Я изучаю Python!'
print(string, string, sep='\n') # Вывод строки string 2 раза с переносом


# Это комментарий.
# Все, что находится на строке после символа
# будет проигнорированно интерпретатором.
# В pyCharm закомментировать строку можно сочетанием клавиш ctrl + /


# Пример:
def func(*args): # Это функция, мы посмотрим ее на следующих занятиях
    return args  # Главное, что можно оставлять комментарий рядом с кодом


#
"""
Документирование кода (Docstrings) или многострочный комментарий 

Документирование кода — неотъемлемая часть разработки на Python. 
Порой документации в коде может быть больше, чем самого кода. 
Она помогает понять, что делает функция или класс, какие аргументы 
принимает и что возвращает.

Для создания docstring используются тройные кавычки : 
''' Docstring'''
 
 """



def fucn(*args):
    """ Пример использования docstring
    функция func() принимает любое число аргументов и возвращает кортеж
    """
    return args