import random
from random import randint

full_list = [1, 2, 3, 4, 5, 6, 7, 9]
# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# full_list = [1, 1, 2, 1]
# full_list = [6, 3, 7]


res_list = []
if full_list:
    first = full_list[0]
    th_num = full_list[2]
    last_element = full_list[-2]
    res_list = (first, th_num, last_element)
    print(res_list)


rand_list = [randint(3, 10) for num in range(10)]
print(rand_list)
# print(rand_list[::3])

# print(random.choice(full_list))
