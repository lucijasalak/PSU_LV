
try:
    unos = float (input("Unesite ocjenu izmedju 0.0 i 1.0: "))
    ocjena = float(unos)
    if ocjena < 0.0 or ocjena > 1.0: 
        print ("Greska! Ocjena mora biti u intervalu 0.0 - 1.0")
    elif ocjena >= 0.9:
        print("Ocjena A")
    elif ocjena >= 0.8:
        print("Ocjena B")
    elif ocjena >= 0.7:
        print("Ocjena C")
    elif ocjena >= 0.6:
        print("Ocjena D")
    else:
        print("Ocjena F")
except:
    print("Greska! Pokusajte ponovno!")