a = input("1ci oyuncu (das/k/qayci/kagiz) daxil edin:")
b = input("2ci oyuncu (das/k/qayci/kagiz) daxil edin:")
if a != "das" and a != "qayci" and a != "kagiz":
    print ("Bele secim yoxdur:")
else:
    if b != "das" and b != "qayci" and b != "kagiz":
        print ("Bele secim yoxdur:")
    else:
        if a == b:
            print ("Berabere:")
        else:
            if a == "das" and b == "qayci":
                print ("1ci oyuncu qazandi:")
            else:
                if a == "qayci" and b == "kagiz":
                    print ("1ci oyuncu qazandi:")
                else:
                    if a == "kagiz" and b == "das":
                        print ("1ci oyuncu qazandi:")
                    else:
                        print ("2ci oyuncu qazandi:")
