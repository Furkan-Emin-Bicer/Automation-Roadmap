birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

ikibasamakli = int(input('Lütfen iki basamaklı sayı giriniz='))

def sayiatama(ikibasamakli):
    if ikibasamakli >= 10 and ikibasamakli <= 99:
        okunacakSayi = ikibasamakli
        return sayiokunusu(okunacakSayi)
    else:
        ikibasamakli = int(input('Lütfen iki basamaklı sayı giriniz='))
        return sayiatama(ikibasamakli)


def sayiokunusu(okunacaksayi):
    birinci = okunacaksayi % 10
    ikinci = okunacaksayi // 10
    sayiOku = onlar[ikinci] + " " + birler[birinci]
    return sayiOku


a = sayiatama(ikibasamakli)
print(a)
