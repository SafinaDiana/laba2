def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

odd_numbers = get_number()

first = None
fifth = None
last = None

for i, value in enumerate(odd_numbers):
    if i == 0:
        first = value
    if i == 4:
        fifth = value
    last = value

print(f"Первое нечетное число: {first}")
print(f"Пятое нечетное число: {fifth}")
print(f"Последнее нечетное число: {last}")