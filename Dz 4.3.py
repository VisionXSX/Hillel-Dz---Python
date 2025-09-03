import random
length = random.randint(3, 10)
numbers = [random.randint(1, 100) for _ in range(length)]
print(numbers)

result = [numbers[0], numbers[2], numbers[-2]]
print(result)