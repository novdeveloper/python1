#Написать программу, которая на любой вопрос отвечает "да" или "нет".

#импортируем нужные библиотеки
from pprint import pprint
import random

pprint("Задайте вопрос: ")
domand = input()
a = []
for i in range(1):
    a.append(random.randint(0, 1))

if a[0] == 0:
    print("нет")
else:
    print("да")