print("Kodlama.io") # print() fonksiyonu ekrana yazı yazdırmak için kullanılır.

# Değişkenler
""" 
Değişkenler, programlama dillerinde verileri saklamak için kullanılan isimlendirilmiş yer tutuculardır. Ayrıca print() ile yazdırmaktansa ileride güncellemek daha kolaydır. 
Değişken değerlerini değiştirebiliriz.
"""
baslik = "Taşıt Kredisi" # baslik değişkenine "Taşıt Kredisi" değerini atadık.

print(baslik) 

# Veri Türleri
# string => metinsel veri
baslik = "İhtiyaç Kredisi"
print(baslik)

#int integer => tam sayı
vade = 36
print(vade)

# float => ondalıklı sayı
aylikOdeme = 200.5
print(aylikOdeme)

# bool => mantıksal veri True/False
yukselistemi = True
print(yukselistemi)


# Matematiksel İşlemler
# Toplama + 
# Çıkarma -
# Çarpma *
# Bölme /
# Üs alma **
# Mod alma %
# Tam Bölme //

print(5+5)
print(vade + 12)
ekvade = 6
print(vade + ekvade)
print(36+6)


print(5 - 5)
print(vade - 12)
print(vade - ekvade)
print(36-6)

print(5 * 5)
print(vade * 12)
print(vade * ekvade)
print(36*6)

print(5 / 5)
print(vade / 12)
print(vade / ekvade)
print(36/6)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20
print(indirimliFiyat)
print(yeniVade)

print(10 % 2)
print(vade % 5)
print(vade % ekvade)
print(30 % 10)

# Mantıksal Operatörleri
"""
Belirli bir koşulu kontrol etmek için kullanılır.
== => eşitse
!= => eşit değilse
> => büyükse
< => küçükse
<= => küçük veya eşitse
>= => büyük veya eşitse

"""

print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# and => ve her iki koşul da doğruysa True diğer durumlarda False
# or => veya her iki koşuldan biri doğruysa True diğer durumlarda False

print(1 > 2 or 5 > 2)
print(1 > 2 and 5 < 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 < 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

# Karar Yapıları
"""
if => eğer
elif => eğer değilse
else => değilse

if koşul:
    koşul sağlandığında yapılacak işlemler
elif koşul2:
    koşul2 sağlanmadığında yapılacak işlemler
else:
    koşullar sağlanmadığında yapılacak işlemler
"""
sayi1 = 30
sayi2 = 20

if sayi1 > sayi2:
    print("Sayı 1 Sayı 2'den büyüktür.")
    print("Hala if bloğunun içindeyiz.")
print("if bloğunun dışındayız.")


if sayi1 < sayi2:
    print("Sayı 1 Sayı 2'den küçüktür.")
elif sayi1 > sayi2:
    print("Sayı 1 Sayı 2'den büyüktür.")
else:
    print("Sayılar eşittir.")
