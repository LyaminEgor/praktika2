country = input("Введите название страны из двух слов: ")

# Разделяем название на два слова
words = country.split()

# Выводим каждое слово с новой строки
for word in words:
    print(word)
