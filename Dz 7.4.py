def common_elements():
    mult_of_3 = set(x for x in range(100) if x % 3 == 0)
    mult_of_5 = set(x for x in range(100) if x % 5 == 0)
    return mult_of_3 & mult_of_5

assert common_elements() == {0, 15, 30, 45, 60, 75, 90} 
print('OK')