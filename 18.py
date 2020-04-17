#Написать программу, которая на любой вопрос отвечает "да" или "нет".

#импортируем нужные библиотеки
from pprint import pprint
import random

pprint("Задайте вопрос: ")
domand = input()


if random.randint(0, 1) == 0:
    print("нет")
else:
    print("да")