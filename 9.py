python
# Задаем количество семей и количество добытых быков
num_families = 7
num_bulls = 33

# Вычисляем сколько быков достанется каждой семье
bulls_per_family = num_bulls // num_families

# Вычисляем количество оставшихся быков
remaining_bulls = num_bulls % num_families

# Выводим результат
print(f"Каждая семья получит {bulls_per_family} быка(ков), а {remaining_bulls} быка(ков) придется отпустить на волю")
