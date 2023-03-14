""" 
AMAÇ:

Derste gördüğümüz "Değişkenler" ve "Şart Blokları" konularının pekiştirilmesi.



ÖDEV TANIMI:

Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.

Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.

Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
"""


""" 
Veri Tipleri
- int => Tam sayılardır. Örnek olarak 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 gibi sayılar tam sayıdır.

- float => Ondalıklı sayılardır. Örnek olarak 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10 gibi sayılar ondalıklı sayıdır.

- String => Metinsel verilerdir. Örnek olarak "Kodlama.io" gibi bir ifade metinsel veridir. Tek tırnak veya çift tırnak içerisinde yazılabilir.

- Boolean => Mantıksal verilerdir. Örnek olarak True veya False gibi ifadeler mantıksal verilerdir.

- list => Liste veri tipi birden fazla veriyi bir arada tutmak için kullanılır. Örnek olarak [1, 2, 3, 4, 5] gibi bir liste oluşturulabilir.

- set => Set veri tipi birden fazla veriyi bir arada tutmak için kullanılır. Örnek olarak {1, 2, 3, 4, 5} gibi bir set oluşturulabilir. Her bir veri bir kez kullanılır. 

- tuple => Tuple veri tipi birden fazla veriyi bir arada tutmak için kullanılır. Örnek olarak (1, 2, 3, 4, 5) gibi bir tuple oluşturulabilir. Tuple veri tipi değiştirilemez.

- dictionary => Dictionary veri tipi birden fazla veriyi bir arada tutmak için kullanılır. Örnek olarak {"bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5} gibi bir dictionary oluşturulabilir. Dictionary veri tipi anahtar ve değer olarak kullanılır.

"""


mail = "berkcan"
sifre = "123456"

email = input("Mail: ")
password = input("Şifre: ")

if mail == email and sifre == password:
    print("Giriş Başarılı")
elif mail != email and sifre == password:
    print("Kullanıcı Adı Hatalı")
elif mail == email and sifre != password:
    print("Şifre Hatalı")
else:
    print("Kullanıcı Adı ve Şifre Hatalı")


kursaKayit = True
if kursaKayit:
    print("Kursa Kayıt Oldunuz. Kurs İçeriğine Giriş Yapabilirsiniz.")
else:
    print("Kursa Kayıt Olmadınız. Kurs İçeriğine Giriş Yapamazsınız.")


kurslar = ["Yazılım Geliştirici Yetiştirme Kampı (JAVA + REACT)","(2022) Yazılım Geliştirici Yetiştirme Kampı - JAVA", "Yazılım Geliştirici Yetiştirme Kampı (JavaScript)", "Yazılım Geliştirici Yetiştirme Kampı (C# + ANGULAR)", "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium"]

egitmenler=["Engin demiroğ","Halit kalaycı"]


for kurs in kurslar:
    print(kurs)


for egitmen in egitmenler:
    print(egitmen)
    
