print("Diga me um número")
num = int(input(""))

if num % 5 == 0:
    print ("FIZZ")

elif num % 3 == 0:
    print ("BUZZ")

elif num % 15 == 0:
    print ("FIZZBUZZ")

else:
    print ("num")
