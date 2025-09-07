seconds = input("Введіть кількість секунд (від 0 до 8640000): ")
total_seconds = int(seconds)
days, remain = divmod(total_seconds, 86400)
hours, remain = divmod(remain, 3600)
minutes, seconds = divmod(remain, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
