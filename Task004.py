#4. Реализуйте алгоритм перемешивания списка.
# Через shuffle
import random
some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(some_list)
print(some_list)
# Через random

second_list = []
for i in range(len(some_list)):
    n = random.randrange(len(some_list))
    i += n
    if i < len(some_list):
        second_list.append(some_list[i])
        
    else:
        i -= len(some_list)
        second_list.append(some_list[i])
print(second_list)