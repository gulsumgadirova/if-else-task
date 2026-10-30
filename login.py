email = "gulsum@gmail.com"
password = "123456789"
e = input ("Emailinizi daxil edin:")
p = input ("Parolunuzu daxil edin:")
if e != email:
    print ("Hesab tapilmadi:")
else:
    if p != password:
        print ("Parol yanlisdir:")
    else:
        print ("Xos geldiniz:")
