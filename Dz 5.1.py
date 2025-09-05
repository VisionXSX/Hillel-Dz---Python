import string
import keyword

name = input("Введіть ім'я змінної: ")
result = True

if name in keyword.kwlist:
    result = False
elif not name:
    result = False
elif name[0].isdigit():
    result = False
elif any(c.isupper() for c in name):
    result = False
elif ' ' in name:
    result = False
elif any(c in string.punctuation and c != '_' for c in name):
    result = False
elif name.count('_') > 1:
    result = False

print(result)
