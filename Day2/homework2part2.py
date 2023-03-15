class Matematik:
    def __init__(self,sayi1,sayi2): # Constructor
        self.s1 = sayi1
        self.s2 = sayi2
        print("Matematik sınıfı başlatıldı.")
    def topla(self):
        return self.s1 + self.s2
    
    def cikar(self):
        return self.s1 - self.s2

    def bol(self):
        return self.s1 / self.s2

    def carp(self):
        return self.s1 * self.s2

matematik = Matematik(5,3)
sonuc = matematik.carp()
print(sonuc)


class Istatistik(Matematik):
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)
    def varyansHesapla(self):
        return self.s1 * self.s2

istatistik = Istatistik(5,3)
