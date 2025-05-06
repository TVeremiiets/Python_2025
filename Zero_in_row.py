zero_in_row = [0, 1, 0, 12, 3]
# zero_in_row = [0]
# zero_in_row = [1, 0, 13, 0, 0, 0, 5]
# zero_in_row = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

tab1, tab2 = [], []
for zero in zero_in_row:
    if zero:
        tab1.append(zero)
    else:
        tab2.append(zero)
print(*(tab1 + tab2))

# variant2

for i in range(len(zero_in_row) - 1, -1, -1):
    if zero_in_row[i] == 0:
        zero_in_row.append(zero_in_row.pop(i))
print(zero_in_row)
