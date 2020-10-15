a = input('Введи строку: ')
mas = []
for i in a:
    mas.append(ord(i))

k = ''
while type(k) != int():
    try:
        k = int(input('Введи шаг: '))
        break
    except ValueError:
        print('Вы ввели не число')

new_mas = []
for i in mas:
    if 65 <= i <= 90:
        i += k
        if i > 90:
            i = (i % 90) + 65
        new_mas.append(i)
    elif 97 <= i <= 122:
        i += k
        if i > 122:
            i = (i % 122) + 97
        new_mas.append(i)
    elif 1040 <= i <= 1071:
        i += k % 33
        if i > 1071:
            i = (i % 1071) + 1040
        new_mas.append(i)
    elif 1072 <= i <= 1103:
        i += k % 33
        if i > 1103:
            i = (i % 1103) + 1072
        new_mas.append(i)
    else:
        new_mas.append(i)

s = str()
for i in new_mas:
    s += chr(i)

print(s)
