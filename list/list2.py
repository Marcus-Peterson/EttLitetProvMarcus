""" skapa en list-variabel med namnet:
lista  
fyll den med udda tal från 0, 20 genom att använda range
Tips: range kan ta 3 argument
"""

lista = list()
for i in range(0,21):
    if i % 2 == 1:
        lista.append(i)
    else:
        continue

print(lista)

