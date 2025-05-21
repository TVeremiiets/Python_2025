my_number = input("Enter whole number: ")

if my_number.lstrip('-').isdigit():
    n = abs(int(my_number))
    while n > 9:
        product = 1
        while n > 0:
            digit = n % 10
            product *= digit
            n //= 10
        n = product

    print("Result:", n)
else:
    print("needs to enter whole number.")