import string

text = input("Введіть текст: ")
text = text.translate(str.maketrans('', '', string.punctuation))
words = [word.capitalize() for word in text.split()]
hashtag = '#' + ''.join(words)
print(hashtag[:140])
