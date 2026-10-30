yas = int(input("Yasinizi daxil edin:"))
telebe = input("Telebesiniz? (beli/xeyr):")
if yas < 7:
    print ("Pulsuz:")
else:
    if yas > 65:
        print ("4 AZN:")
    else:
        if telebe == "beli":
            print ("5 AZN:")
        else :
            print ("8 AZN:")
