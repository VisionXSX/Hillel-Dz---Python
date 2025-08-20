a = float(input("Введіть перше число: "))
sign = input("Введіть дію (+, -, *, /): ")
b = float(input("Введіть друге число: "))

if sign == '+':
    print(a + b)
elif sign == '-':
    print(a - b)
elif sign == '*':
    print( a * b)
elif sign == '/':
    if b == 0:
        print("Помилка: Ділення на нуль неможливе!")
    else:
        print(a / b)