eded = int(input("Eded daxil et:"))
if eded % 3 == 0 and eded % 5 == 0:
   print ("FizzBuzz:")
else:
    if eded % 3 == 0:
         print ("Fizz:")
    else:
     if eded % 5 == 0:
         print ("Buzz:")
     else:
        print (eded)
