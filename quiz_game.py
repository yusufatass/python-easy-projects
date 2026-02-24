print("Welcome to the Computer Quiz! 💻\n")

# Kullanıcı girişindeki boşlukları temizlemek ve küçük harfe çevirmek için .strip().lower() kullan
playing = input("Do you want to play? (yes/no): ").strip().lower()

if playing not in ["yes", "y"]:
    print("Maybe next time. Goodbye!")
    quit()

print("\nOkay! Let's GOOO! 🚀\n")

score = 0

# Soruları ve cevapları bir sözlük (dictionary) listesi içinde tutuyoruz.
# Bu sayede yeni soru eklemek çok daha kolay olur.
quiz_data = [
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "What does GPU stand for?", "answer": "graphics processing unit"},
    {"question": "What does RAM stand for?", "answer": "random access memory"},
    {"question": "What does PSU stand for?", "answer": "power supply unit"}
]

total_questions = len(quiz_data)

# Soru listesi üzerinde döngüye giriyoruz
for i, item in enumerate(quiz_data, start=1):
    answer = input(f"Q{i}: {item['question']}\nYour answer: ").strip().lower()

    if answer == item["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        # Yanlış cevap durumunda doğru cevabı da gösteriyoruz
        print(f"❌ Incorrect! The correct answer is: {item['answer'].title()}\n")

print("-" * 30)
print(f"You got {score} out of {total_questions} questions correct!")

# Yüzdeyi sabit bir sayıya (4) bölmek yerine, listenin uzunluğuna bölerek dinamik hale getir
percentage = (score / total_questions) * 100

# .2f ile virgülden sonra sadece 2 basamak göster
print(f"Your score: %{percentage:.2f} 🎯")