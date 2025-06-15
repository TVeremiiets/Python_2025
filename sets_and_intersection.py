def common_elements():
    list_num3 = {x for x in range(100) if x % 3 == 0}
    list_num5 = {x for x in range(100) if x % 5 == 0}
    return list_num3 & list_num5

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}

