mesafe = float(input("Mesafeni daxil edin:"))
saat = int(input("Saati daxil edin (0-23):"))
if mesafe < 0 or saat < 0 or saat > 23:
    print ("Yanlis melumat:")
else:
    qiymet = 2 + mesafe * 0.80
    if saat >= 23 or saat < 6:
        qiymet = qiymet * 1.20
        if qiymet < 3:
            qiymet = 3
    print ("Qiymet:", qiymet, "AZN")