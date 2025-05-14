from re import sub

my_row='Python Community'
#print(my_row)
#my_row='i like python community!'
#my_row='Should, I. subscribe? Yes!'

print(my_row)
print('#' + sub(r'(?:^|\W+)(\w)?', lambda x: x.group(1).upper() if x.group(1) else '', my_row)[:140])

