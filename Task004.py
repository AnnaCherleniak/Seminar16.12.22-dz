#4. Реализуйте алгоритм перемешивания списка.
# Через shuffle
import random
some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(some_list)
print(some_list)

# Через random
second_list = []
while len(second_list) != len(some_list):
    i = random.randrange(len(some_list))
    if some_list[i] not in second_list:
        second_list.append(some_list[i])
print(second_list)


