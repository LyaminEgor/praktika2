weight = float(input("Введите вес (в фунтах): "))
height = float(input("Введите рост (в дюймах): "))

# Формула для вычисления ИМТ: вес / (рост * рост)
bmi = (weight / (height * height)) * 703

print("ИМТ:", format(bmi, ".2f"))