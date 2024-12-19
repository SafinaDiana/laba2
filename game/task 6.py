import random

def rock_paper_scissors():
    print("Добро пожаловать в игру 'Камень-ножницы-бумага'!")
    choices = ["Камень", "Ножницы", "Бумага"]

    while True:
        player_choice = input("Выберите Камень, Ножницы или Бумага (или 'выход' для завершения): ").capitalize()
        if player_choice == "Выход":
            print("Спасибо за игру! До встречи!")
            break

        if player_choice not in choices:
            print("Некорректный ввод. Пожалуйста, выберите Камень, Ножницы или Бумага.")
            continue

        computer_choice = random.choice(choices)
        print(f"Вы выбрали: {player_choice}")
        print(f"Компьютер выбрал: {computer_choice}")

        if player_choice == computer_choice:
            print("Ничья!")
        elif (player_choice == "Камень" and computer_choice == "Ножницы") or \
             (player_choice == "Ножницы" and computer_choice == "Бумага") or \
             (player_choice == "Бумага" and computer_choice == "Камень"):
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")

        print()  

rock_paper_scissors()
