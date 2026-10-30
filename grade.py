bal = int(input("Bal daxil edin:"))
if bal < 0 or bal > 100:
    print ("Yanlis bal:")
else:
    if bal >= 91:
        print ("A:")
    else:
        if bal >= 81:
            print ("B:")
        else:
            if bal >= 71:
                print ("C:")
            else:
                if bal >= 61:
                    print ("D:")
                else:
                    print ("F:")    