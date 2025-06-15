
#while operation != 0:
first_num = int(input("Enter the first number"))
second_num = int(input("Enter the second number"))
print ("actions - if plus enter 1, If minus enter 2, multiplication enter 3, division enter 4")
operation = int(input("Select what action is needed"))

#while operation != 0:
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




