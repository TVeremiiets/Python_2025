my_list = [12, 3, 4, 10]
my_list = []
my_list = [1]
# my_list = [12, 3, 4, 10, 8]

print(f"{my_list} => {my_list[-1:]+my_list[:-1]}")

# variant2
if my_list:
    last_element = my_list.pop()
    my_list.insert(0, last_element)
print(my_list)
