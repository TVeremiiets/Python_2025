import string

user_input = input("Enter two letters using '-' (example, a-f or a-A): ")

start, end = user_input.split('-')
all_letters = string.ascii_letters

collecting = False
result = ''

for char in all_letters:
    if char == start:
        collecting = True
    if collecting:
        result += char
    if char == end:
        break

print(result)