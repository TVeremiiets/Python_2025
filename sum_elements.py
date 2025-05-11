calc_list = [0, 1, 7, 2, 4, 8]
# calc_list = [1, 3, 5]
# calc_list = [6]
# calc_list = []

res_sum = 0

for num in range(len(calc_list)):
    if num % 2 == 0:
        res_sum += calc_list[num]
#        print(res_sum)
print(res_sum * calc_list.pop())
