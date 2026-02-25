from playsound import playsound
import time
import os

# ANSI Kaçış Kodları (Terminal ekranını kontrol etmek için kullanılır)
CLEAR = "\033[2J"  # Tüm terminal ekranını temizler
CLEAR_AND_RETURN = "\033[H"  # İmleci (cursor) en sol üste geri taşır


def alarm(seconds):
    """
    Belirtilen saniye boyunca geri sayım yapar ve süre bitince alarm çalar.
    """
    time_elapsed = 0

    # Döngü başlamadan önce terminali tamamen temizle
    print(CLEAR)

    # Geçen süre, istenen süreye ulaşana kadar döngüye devam et
    while time_elapsed < seconds:
        time.sleep(1)  # Programı 1 saniye beklet
        time_elapsed += 1

        # Kalan süreyi hesapla
        time_left = seconds - time_elapsed

        # Saniyeyi dakika ve saniye formatına çevir
        # Örnek: 125 saniye -> 125 // 60 = 2 dakika | 125 % 60 = 5 saniye
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Sayacın tek satırda güncellenmesi için CLEAR_AND_RETURN kullanıyoruz
        # :02d formatı, sayı tek haneliyse başına 0 ekler (Örn: 5 yerine 05)
        print(f"{CLEAR_AND_RETURN}⏰ Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    # Süre dolduğunda döngü biter ve aşağıdaki kod çalışır
    print("\nTime is up! 🔔")

    try:
        # Ses dosyasının tam yolunu bularak playsound'un çökmesini engelliyoruz
        base_dir = os.path.dirname(__file__)
        sound_path = os.path.join(base_dir, "alarm.mp3")
        playsound(sound_path)
    except Exception as e:
        print(f"Error playing sound: {e}")


# ==========================================
# ANA UYGULAMA (Kullanıcıdan veri alma)
# ==========================================

print("Welcome to the Python Alarm Clock! ⏲️\n")

# Kullanıcının yanlışlıkla harf girmesine karşı programı koruyoruz
try:
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))

    total = minutes * 60 + seconds

    if total > 0:
        alarm(total)
    else:
        print("Please enter a time greater than 0.")

except ValueError:
    print("Invalid input! Please enter numbers only.")