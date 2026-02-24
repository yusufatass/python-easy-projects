import random

user_wins = 0
computer_wins = 0
draws = 0  # Beraberlikleri de saymak güzel bir istatistik olabilir

options = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors! 🪨 📄 ✂️\n")

while True:
    # .strip() ile gereksiz boşlukları engelliyoruz
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").strip().lower()

    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please try again.")
        continue

    # İşte Pythonic yöntem: Listeden doğrudan rastgele seçim yap!
    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    # 1. Önce beraberliği kontrol et
    if user_input == computer_pick:
        print("It's a draw! 🤝")
        draws += 1

    # 2. Kullanıcının kazanma durumlarını tek bir if/elif bloğunda birleştir
    elif (user_input == "rock" and computer_pick == "scissors") or \
            (user_input == "paper" and computer_pick == "rock") or \
            (user_input == "scissors" and computer_pick == "paper"):
        print("You win! 🎉")
        user_wins += 1

    # 3. Geriye kalan tek ihtimal bilgisayarın kazanmasıdır
    else:
        print("You lose! 😢")
        computer_wins += 1

print("-" * 30)
# F-string ile sonuç tablosunu daha şık hale getirelim
print(f"Final Score -> User: {user_wins} | Computer: {computer_wins} | Draws: {draws}")

if user_wins == computer_wins:
    print("It's a tie overall!")
elif user_wins > computer_wins:
    print("You won the game! 🏆")
else:
    print("Computer won the game! 🤖")

print("Goodbye! 👋")