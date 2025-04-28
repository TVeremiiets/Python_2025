# + : 1
# - : 1
# * : 3
# / : 4

operation = int(1)

while operation != 0:
    first_num = int(9)
    second_num = int(3)

    if operation == 0:
        break        # print('Please select operation')
    if operation == 1:
        print(first_num + second_num)
    elif operation == 2:
        print(first_num - second_num)
    elif operation == 3:
        print(first_num * second_num)
    elif operation == 4:
        if second_num == 0:
            print('You cant divide by zero!')
        else:
            print(first_num // second_num)
    else:
        print('Incorrect operation')
    operation = int(input())



