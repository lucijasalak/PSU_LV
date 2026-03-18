

brojevi = []

while True:
    unos = input ()
    if unos == "Done":
        break
    unos = float(unos)
    brojevi.append(unos)

if len (brojevi) == 0:
    print ("Unesite brojeve!")
else:
    print(brojevi)
    print(len(brojevi))
    print(min(brojevi))
    print(max(brojevi))
    print(sum(brojevi)/len(brojevi))

brojevi.sort()
print(brojevi)