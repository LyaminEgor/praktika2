# Предполагаем, что все люди и животные направляются в Сент-Айвс

# Рассчитываем количество кошек
wives = 7
bags_per_wife = 7
cats_per_bag = 7
total_cats = wives * bags_per_wife * cats_per_bag

# Рассчитываем количество котят
kittens_per_cat = 7
total_kittens = total_cats * kittens_per_cat

# Рассчитываем общее количество людей и животных
total_people_and_animals = 2 + wives + total_cats + total_kittens

print("Общее число людей и животных, направляющихся в Сент-Айвс:", total_people_and_animals)
