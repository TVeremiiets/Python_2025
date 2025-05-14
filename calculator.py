def f_num_s_num():
    f_num = float(input("Enter the first number:  "))
    s_num = float(input("Enter the second number:  "))
    return f_num, s_num

calc = input("Do we do calculations? (`yes` или `no`- exit) ")

while calc != 'no':
    print()
    f_num, s_num = f_num_s_num()

    oper = input("Select what action is needed (+, -, * or /) :  ")

    if (oper == "+"):
        res = f_num + s_num
    elif (oper == "-"):
        res = f_num - s_num
    elif (oper == "*"):
        res = f_num * s_num
    elif (oper == "/"):
        if s_num == 0:
            print('You cant divide by zero!')
        else:
            res = f_num / s_num
    else:
        res = ""
        oper = "incorrect operation, please try again"

    print("\n{} {} {} = {}".format(f_num, oper, s_num, res))

    calc = input("\nDo you want to continue calculating? (`yes` или `no`- exit) ")
