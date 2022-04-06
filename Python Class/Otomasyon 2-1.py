class Ogrenci:
    def __init__(self, ogrenciadi, ogrencisoyadi, ogrencisinif):
        self.ogrenciadi = ogrenciadi
        self.ogrencisoyadi = ogrencisoyadi
        self.ogrencisinif = ogrencisinif

    def ogrenci_bilgi(self):
        print("Adı:", self.ogrenciadi, "Soyadı:", self.ogrencisoyadi, "Sınıfı:", self.ogrencisinif)


class Soru:
    def __init__(self):
        self.dogru = int(input("Doğru Sayısı:"))
        self.yanlis = int(input("Yanlış sayısı:"))

    def net_sayisi(self):
        sorusayisi = self.dogru + self.yanlis
        if sorusayisi <= 50:
            self.goturen = int(self.yanlis / 4)
            self.net = self.dogru - self.goturen
            return self.net
        else:
            print("Toplam 50 ya da daha az soru sayısı olmalı!!!!!")
            quit()

    def hesapla(self, net):
        self.puan = self.net * 2
        if self.puan < 0:
            self.puan = 0
        return self.puan


ogrenci1 = Ogrenci("Furkan ", "Biçer", "12")
sinav1 = Soru()
ogrenci1.ogrenci_bilgi()
print("Sınav Puanı:", sinav1.hesapla(sinav1.net_sayisi()))
