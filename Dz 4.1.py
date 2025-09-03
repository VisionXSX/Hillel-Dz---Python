lst = [0, 1, 0, 12, 3]
    
non_zeros = [x for x in lst if x != 0]
zeros = [x for x in lst if x == 0]
result = non_zeros + zeros
print(list(result))          