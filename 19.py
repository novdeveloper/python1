#Сделать так что бы она помнила отвеченные вопросы.

#импортируем нужные библиотеки
from pprint import pprint
import random

question = ""
save = []

#цикл для ввода вопроса
while question != "хватит":
    pprint("Задайте вопрос (для выхода введите хватит): ")
    question = input()
#сохраняем в список save все вопросы    
    save.append(question)

#рандомный ответ с сохранением его в save    
    if random.randint(0, 1) == 0:        
        print("нет")
        save.append("нет")
    else:
        print("да")
        save.append("да")
#вывод всех записанных вопросов и ответов
print(save)