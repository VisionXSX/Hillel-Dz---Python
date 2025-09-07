import string

letters = string.ascii_letters
start, end = input().split('-')
start_idx = letters.index(start)
end_idx = letters.index(end)

print(letters[start_idx:end_idx+1])