from re import sub
import string
from shlex import join

my_row='Python Community'
print(my_row)
#my_row='i like python community!'
#my_row='Should, I. subscribe? Yes!'

#variant1
print('#' + sub(r'(?:^|\W+)(\w)?', lambda x: x.group(1).upper() if x.group(1) else '', my_row)[:140])
#print('#' + ''.join(map(lambda x: join(filter(str.isalnum, my_row)).capitalize(), input().split()))[:140])

#variant2
print('#' + ''.join(map(lambda x: x.capitalize(), ''.join(filter(str.isalnum, my_row)).split()))[:140])
print('#' + ''.join(map(lambda x: x.upper(), ''.join(filter(str.isalnum, my_row)).split()))[:140])