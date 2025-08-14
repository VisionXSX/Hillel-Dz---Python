number = int(input("Введіть 5-ти значне число: "))

rebmun = 0
for i in range(5): 
    rebmun = rebmun * 10 + number % 10
    number //= 10
print(rebmun)