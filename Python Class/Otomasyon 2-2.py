class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return f' Ad:{self.ad}, Soyad:{self.soyad}, Yaş:{self.yas}, Ülke:{self.ulke}, Şehir:{self.sehir}'

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


yeni_insan = Insan("Furkan", "Biçer", "22", "Türkiye", "Yozgard")
yeni_insan.yetenek_ekle('C#')
yeni_insan.yetenek_ekle('Python')
yeni_insan.yetenek_ekle('Unity')
print(yeni_insan.kisi_bilgileri())
print(yeni_insan.yetenekler)
