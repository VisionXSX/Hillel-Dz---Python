lst = [0, 1, 7, 2, 4, 8]

if len(lst) == 0 or lst == [0]:
    print(0)
else:
    numbers = sum(lst[i] for i in range(0, len(lst), 2))
    sum = [lst[i] for i in range(0, len(lst), 2)]
    print(numbers * (lst[-1]))
