ceki = float(input("Cekini daxil edin:"))
bilet = input("Bilet novu (econom/business):")
if ceki < 0:
    print ("Yanlis ceki:")
else:
    if ceki > 32:
        print ("Baqaj qebul edilmir:")
    else:
        if bilet == "econom":
            if ceki <= 23:
                print ("Baqaj pulsuz:")
            else:
                print ("30 AZN")
        else:
            if bilet == "business":
                print ("Baqaj pulsuz:")
            else:
                print ("Yanlis bilet novunu daxil etmisiniz:")
                