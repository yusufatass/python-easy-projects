# 🐍 Python Beginner Projects (Yeni Başlayanlar İçin Python Projeleri)

Merhaba! 👋 Kodlama dünyasına yeni adım atıyorsanız, doğru yerdesiniz. Bu depo (repository), Python öğrenmeye yeni başlayanlar için temel programlama mantığını kavratmak amacıyla hazırlanmış eğlenceli, basit ve öğretici projeler içermektedir.

Buradaki kodları inceleyerek **değişkenler, döngüler (`while`, `for`), koşullu ifadeler (`if`, `elif`, `else`) ve kullanıcı girdisi alma (`input`)** gibi temel konuların gerçek projelerde nasıl kullanıldığını pratik bir şekilde görebilirsiniz.

---

## 📂 Depo İçeriği ve Projeler

Bu repoda şu an temel Python mantığını kavratacak farklı mini projeler bulunmaktadır:

### 1. 🧠 Bilgi Yarışması (`quiz_game.py`)
Kullanıcıya bilgisayar donanımları hakkında çeşitli soruların sorulduğu ve doğru cevapların puanlandığı basit bir bilgi yarışması uygulamasıdır.
* **Ne Öğretir?** Kullanıcıdan veri alma (`input`), string (metin) manipülasyonu, `if/else` koşulları ve değişkenler üzerinden skor tutma/hesaplama.

### 2. 🎲 Sayı Tahmin Oyunu (`number_guesser.py`)
Bilgisayarın belirlediğiniz bir aralıkta rastgele tuttuğu sayıyı bulmaya çalıştığınız bir oyundur. Yanlış tahminlerde "Daha yukarı" veya "Daha aşağı" şeklinde ipuçları verir.
* **Ne Öğretir?** `random` modülünün kullanımı, `while True` sonsuz döngüleri, veri tipi dönüşümleri (metinden tam sayıya - `int()`) ve döngü kırma (`break/continue`) komutları.

### 3. ✌️ Taş-Kağıt-Makas Oyunu (`roc-paper-scissors.py`)
Bilgisayara karşı oynadığınız klasik Taş-Kağıt-Makas oyunu. Siz ve bilgisayarın seçimleri karşılaştırılır ve kimin kaç el kazandığına dair genel bir skor tablosu tutulur.
* **Ne Öğretir?** Listeler (lists) içinden rastgele eleman seçme (`random.choice()`), karmaşık `if/elif/else` blokları kurgulama ve mantıksal operatörlerin (`and`) kullanımı.

### 4. 🗺️ Metin Tabanlı Macera Oyunu (`choose-ur-adventure.py`)
Yaptığınız seçimlere göre hikayenin gidişatının ve sonunun değiştiği, klasik bir "Kendi Maceranı Seç" tarzı rol yapma oyunudur. Doğru yolu bulup hayatta kalmaya çalışırsınız!
* **Ne Öğretir?** İç içe geçmiş (nested) koşullu ifadeler ve yazılımda "karar ağacı" (decision tree) mantığını kurgulama.

### 5. ⏰ Dijital Alarm Saati (`alarm_clock.py`)
Kullanıcıdan alınan süre boyunca terminal ekranında dinamik olarak (tek bir satır üzerinde) geri sayım yapan ve süre dolduğunda belirlediğiniz bir ses dosyasını (MP3) çalan pratik bir zamanlayıcı uygulamasıdır.
* **Ne Öğretir?** `time` modülü ile zamanı yönetme (`time.sleep`), ANSI kaçış kodlarıyla terminal ekranını temizleyip animasyonlu gibi veri güncelleme, dış kütüphaneler (örn: `playsound` veya `pygame`) kullanarak medya oynatma ve `try-except` bloklarıyla hatalı kullanıcı girişlerini yakalama.

### 6. 🔐 Rastgele Şifre Oluşturucu (`password_generator.py`)
Belirlediğiniz uzunlukta ve kriterlerde (sayı ve özel karakter içerme durumu) kırılması zor, tamamen rastgele şifreler üreten bir güvenlik aracıdır. İstenen tüm güvenlik şartları sağlanana kadar kendi içinde denemeler yapmaya devam eder.
* **Ne Öğretir?** `string` ve `random` modüllerinin kullanımı, `while True` döngüsü ile koşullar sağlanana kadar işlem yapma (yazılımdaki "flag/bayrak" mantığı), boolean mantığı (`True`/`False`) ve fonksiyonlara varsayılan (default) parametreler atama.

---
