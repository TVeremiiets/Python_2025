#2 list
my_first_list = [1, 2, 3, 4, 5, 6]
even, odd = [even for even in my_first_list if even % 2 == 0], [odd for odd in my_first_list if odd % 2 != 0]
print(even,",", odd)

#variant2
even2, odd2 = [], []
for num in my_first_list:
    (even2 if num % 2 == 0 else odd2).append(num)
print(even2,",", odd2)

#unpaired number of elements
my_second_list = [1, 2, 3]
Mylist = [my_second_list[i:i + 2] for i in range(0, len(my_second_list), 2)]
print(Mylist)

#
my_third_list=[1, 2, 3, 4, 5]
ls_1 = sum( tuple( divmod( len(my_third_list), 2 ) ) )
res_list = [ my_third_list[:ls_1], my_third_list[ls_1:] ]
print( res_list )

#empty list
empty_list=[]
empty_list2=empty_list
print(empty_list,",", empty_list2)







