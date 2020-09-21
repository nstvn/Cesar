a = str()
mas = []
for i in a:
    mas.append(ord(i))
print(mas)

k = int()
new_mas = []
for i in mas:
    if i >= 1040 and i <= 1071:
        i += k%33
        if i > 1071:
            i = (i % 1071)+1040
        new_mas.append(i)
    elif i >= 1072 and i <= 1103:
        i += k %33
        if i > 1103:
            i = (i % 1103)+1072
        new_mas.append(i)
    else:
        new_mas.append(i)

s = str()
for i in new_mas:
    s += chr(i)
