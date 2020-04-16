adict = {
        1:"honda, 1999, universal",
        2:"toyota, 1995, sedan",
        3:"lada, 2020, sedan",
        4:"seat, 2002, universal"
        }
print(adict)
print("введите данные автомобиля")
a = input()

for i in adict:
    if a in adict[i]:
        print(adict[i])