vize1 = float(input('Lütfen vize 1 notunu giriniz='))
vize2 = float(input('Lütfen vize 2 notunu giriniz='))
final = float(input('Lütfen final notunu giriniz='))

if (0 <= vize1 <= 100 and 0 <= vize2 <= 100 and 0 <= final <= 100):
    toplamnot = float((vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4))
    if (toplamnot >= 90):
        print('Toplam Not ----->', toplamnot, ' -----> AA -----> Geçtiniz')
    elif (toplamnot >= 85 and toplamnot < 90):
        print('Toplam Not ----->', toplamnot, ' -----> BA -----> Geçtiniz')
    elif (toplamnot >= 80 and toplamnot < 85):
        print('Toplam Not ----->', toplamnot, ' -----> BB -----> Geçtiniz')
    elif (toplamnot >= 75 and toplamnot < 80):
        print('Toplam Not ----->', toplamnot, ' -----> CB -----> Geçtiniz')
    elif (toplamnot >= 70 and toplamnot < 75):
        print('Toplam Not ----->', toplamnot, ' -----> CC -----> Geçtiniz')
    elif (toplamnot >= 65 and toplamnot < 70):
        print('Toplam Not ----->', toplamnot, ' -----> DC -----> Geçtiniz')
    elif (toplamnot >= 60 and toplamnot < 65):
        print('Toplam Not ----->', toplamnot, ' -----> DD -----> Geçtiniz')
    elif (toplamnot >= 55 and toplamnot < 60):
        print('Toplam Not ----->', toplamnot, ' -----> FD -----> Geçtiniz')
    else:
        print('Toplam Not ----->', toplamnot, ' -----> FF -----> Kaldınız')
else:
    print('0-100 arası değer giriniz')
