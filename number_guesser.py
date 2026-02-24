import random

print("Welcome to the Number Guessing Game! 🎲\n")

# 1. Aşama: Geçerli bir üst sınır (top_of_range) alana kadar sormaya devam et
while True:
    top_of_range = input("Type a number for the upper limit: ").strip()

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range > 0:
            break  # Geçerli ve 0'dan büyük bir sayı girildiyse döngüden çık
        else:
            print("Sorry, the number must be greater than 0.")
    else:
        print("Please type a valid number next time.")

# random.randint(1, top_of_range) genelde tahmin oyunları için daha doğaldır (0 yerine 1'den başlatmak)
random_number = random.randint(1, top_of_range)
guesses = 0

print(f"\nOkay! I'm thinking of a number between 1 and {top_of_range}. Let's go!\n")

# 2. Aşama: Tahmin döngüsü
while True:
    user_guess = input("Make a guess: ").strip()

    # Girilen değerin sayı olup olmadığını kontrol et
    if not user_guess.isdigit():
        print("Please type a valid number.")
        continue  # Hatalı girişte döngünün başına dön, tahmini sayma

    user_guess = int(user_guess)
    guesses += 1  # Sadece geçerli bir sayı girildiğinde tahmin sayısını artır

    # Karşılaştırma blokları
    if user_guess == random_number:
        print("🎉 You guessed right!")
        break
    elif user_guess > random_number:
        print("You were above the number. Try going lower ⬇️")
    else:
        print("You were below the number. Try going higher ⬆️")

print("-" * 30)
print(f"Game Over! You guessed the number in {guesses} tries.")