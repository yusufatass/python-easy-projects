import random
import string


def generate_password(min_length=10, include_numbers=True, include_special=True):
    """
    Belirtilen uzunlukta ve kriterlerde rastgele ve güvenli bir şifre oluşturur.
    """
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Karakter havuzunu oluşturuyoruz.
    # istenen tüm kategorileri havuza eklyoruz.
    characters = letters
    if include_numbers:
        characters += digits
    if include_special:
        characters += special

    pwd = ""
    has_number = False
    has_special = False

    # Şifre hem minimum uzunluğa ulaşana kadar hem de kriterleri sağlayana kadar dön!
    while True:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Kriterlerin sağlanıp sağlanmadığını kontrol et
        meets_length = len(pwd) >= min_length
        meets_numbers = not include_numbers or has_number
        meets_special = not include_special or has_special

        # Eğer tüm şartlar sağlandıysa döngüden çık
        if meets_length and meets_numbers and meets_special:
            break

    return pwd


# ==========================================
# ANA UYGULAMA
# ==========================================

print("Şifre Oluşturucuya Hoş Geldiniz! 🔐\n")

# İstersen kullanıcıdan input alarak dinamik hale getirebiliriz:
try:
    length = int(input("Şifreniz en az kaç karakter olsun? (Örn: 12): "))

    # generate_password() fonksiyonunu çağırıyoruz
    secure_password = generate_password(min_length=length)

    print("-" * 30)
    print(f"Oluşturulan Şifreniz: {secure_password}")
    print("-" * 30)

except ValueError:
    print("Lütfen sadece sayı giriniz!")