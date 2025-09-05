while True:
    num1 = float(input("Введіть перше число: "))
    op = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Не діли на нуль!")
            continue
        result = num1 / num2
    print("Результат:", result)
    cont = input("Продовжити? (y/yes): ").strip().lower()
    if cont not in ('y', 'yes'):
        print("Роботу завершено.")
        break