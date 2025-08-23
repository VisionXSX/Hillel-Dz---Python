lst = [1, 2, 3, 4, 5]
a = len(lst) // 2 + len(lst) % 2
b = len(lst) // 2

if b == 0:
    two_lists = [lst[:a],[]]
else:
    two_lists = [lst[:a], lst[-b:]]
print(two_lists)