my_list = [12, 3, 4, 10]
print(f'{my_list} => {my_list[-1:]+my_list[:-1]}')


for x in input(my_list).split():
    my_list.append(int(x))
    my_list.insert(3, my_list.pop())
print(my_list)

