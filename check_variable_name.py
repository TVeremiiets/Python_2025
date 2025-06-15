import string
import keyword

my_row = input("Enter your row: ")
if not my_row.isidentifier():
    print(f"'{my_row}' this is not a valid identifier - not variable name")
elif keyword.iskeyword(my_row):
    print(f"'{my_row}' this is a reserved word - not variable name")
elif my_row[0].isdigit():
    print(f"'{my_row}' can't start with the numbers - not variable name")
elif any(char.isupper() for char in my_row):
    print(f"'{my_row}' capital letters are used - not variable name")
elif any(char in string.punctuation and char != "_" for char in my_row):
    print(f"'{my_row}'  can't use more than one underscore")
elif my_row.count('_') > 1:
    print(f"'{my_row}' more than one underscore used - not variable name")
else:
    print(f"'{my_row}' great, good variable name")