# Kullanıcının isminin baş harfini büyük yazdırmak için .title() ekleyebiliriz
name = input("What is your name? ").strip()
print(f"\nWelcome, {name.title()}, to this epic adventure! 🗺️\n")

print("You are on a dirt road. It has come to an end and you can go 'left' or 'right'.")
choice1 = input("Which way do you want to go? ").strip().lower()

# SOL YOL
if choice1 == "left":
    print("\nYou walk down the left path and come to a deep, rushing river. 🌊")
    choice2 = input("You can 'swim' across or 'walk' along the bank. Which one do you choose? ").strip().lower()

    if choice2 == "swim":
        print("\nYou jumped into the water... but wait! You were eaten by a hungry alligator. 🐊 Game Over!")

    elif choice2 == "walk":
        print("\nYou walked for miles along the riverbank. You are exhausted but you find an old, wooden boat! 🛶")
        choice3 = input("Do you want to 'row' the boat across or 'keep walking'? ").strip().lower()

        if choice3 == "row":
            print("\nYou successfully rowed across the river and found a hidden treasure chest! 🏆 You WIN!")
        elif choice3 == "keep walking":
            print("\nYou walked too far, ran out of water, and collapsed. 🏜️ Game Over!")
        else:
            print("\nYou stood there doing nothing until night fell. The shadows got you. 💀 Game Over!")
    else:
        print("\nInvalid choice. You slipped on the mud and fell into the river anyway. 💦 Game Over!")

# SAĞ YOL
elif choice1 == "right":
    print("\nYou take the right path and enter a dark, mysterious forest. 🌲")
    choice2 = input("You see a glowing 'cave' and a rickety 'bridge'. Where do you go? ").strip().lower()

    if choice2 == "cave":
        print("\nInside the cave, a sleeping dragon wakes up. 🐉 It breathes fire. Game Over!")

    elif choice2 == "bridge":
        print("\nYou carefully cross the bridge and meet a wise old wizard. 🧙‍♂️")
        print("He asks you a riddle: 'I speak without a mouth and hear without ears. What am I?'")

        riddle_answer = input("Your answer: ").strip().lower()

        # Bulmacanın cevabı 'echo' (yankı)
        if riddle_answer == "echo" or riddle_answer == "an echo":
            print("\nThe wizard smiles. 'Correct!' He teleports you to safety with a bag of gold. 💰 You WIN!")
        else:
            print(f"\n'Wrong!' says the wizard. 'The answer was an echo.' He turns you into a frog. 🐸 Game Over!")

    else:
        print("\nYou wandered off the path and got lost forever. 🧭 Game Over!")

# GEÇERSİZ İLK GİRİŞ
else:
    print("\nThat wasn't an option! You stood still for so long that you turned into a tree. 🌳 Game Over!")