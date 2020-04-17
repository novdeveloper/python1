#Написать программу, которая на любой вопрос отвечает "да" или "нет".

#импортируем нужные библиотеки
from pprint import pprint
import random

domand = ""

while domand != "хватит":
    pprint("Задайте вопрос (для выхода введите хватит): ")
    domand = input()
    if random.randint(0, 1) == 0:
        print("нет")
    else:
        print("да")