# Sınıflar
# self keywordünün işlevi => Sınıf içerisindeki değişkenlere erişmek için kullanılır.
class Human:
    name = "Berkcan"
    def __init__(self,name): # __init__ => Constructor
        self.name = name # Bu değişkeni sınıfın içerisinde kullanmak için self keywordü kullanılır.
        print("Bir human instance'i üretildi.")
    def __str__(self):
        return f"STR fonksiyonu çağırıldı. {self.name}"
    # __str__ => Bu fonksiyonu çağırdığımızda bu fonksiyonun içerisindeki değeri döndürür.
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking")

human = Human("Berkcan") # instance (örnek) oluşturduk
human.talk("Merhaba") 
human.walk() 
print(human)

human2 = Human("Ahmet")
#human2.name = "Ahmet"
human2.talk("Merhaba")
human2.walk()
print(human2)


