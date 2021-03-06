a = input('Введи строку: ')
mas = []
for i in a:  # Возвращение числового представления каждого символа строки
    mas.append(ord(i))

k = ''
while type(k) != int():  # Цикл для проверки на ввод числа
    try:  # Проверка на ввод числа
        k = int(input('Введи шаг: '))
        break
    except ValueError:
        print('Вы ввели не число')

new_mas = []
for i in mas:  # Работа с числовыми представлениями строки
    if 65 <= i <= 90:  # Определение заглавных букв английского алфавита
        i += k
        if i > 90:  # Определение выхода за границы
            i = (i % 90) + 65
        new_mas.append(i)
    elif 97 <= i <= 122:  # Определение прописных букв английского алфавита
        i += k
        if i > 122:  # Определение выхода за границы
            i = (i % 122) + 97
        new_mas.append(i)
    elif 1040 <= i <= 1071:  # Определение заглавных букв русского алфавита
        i += k % 33
        if i > 1071:  # Определение выхода за границы
            i = (i % 1071) + 1040
        new_mas.append(i)
    elif 1072 <= i <= 1103:  # Определение прописных букв русского алфавита
        i += k % 33
        if i > 1103:  # Определение выхода за границы
            i = (i % 1103) + 1072
        new_mas.append(i)
    else:  # Пропуск специальных символов и чисел
        new_mas.append(i)

s = str()
for i in new_mas:  # Возвращение символа для каждого числового представления
    s += chr(i)

print(s)  # Вывод зашифрованного текста
