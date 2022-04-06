def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    bolunenSayi = []
    for i in range(min_sayi + 1, max_sayi):
        if i % bolunecek_sayi == 0:
            bolunenSayi.append(i)
        toplamSayi = len(bolunenSayi)
    return toplamSayi, bolunenSayi


a = bolunenSayiBulma(2, 55, 2)
print(a)
