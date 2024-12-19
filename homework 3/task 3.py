from datetime import datetime

def calculate_age():
    try:
        birth_date = input("Введите дату рождения в формате ДД/ММ/ГГГГ: ")
        birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
        
        today = datetime.today()
        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print(f"Ваш возраст: {age} лет.")
    except ValueError:
        print("Ошибка: Неверный формат даты. Попробуйте снова.")

calculate_age()